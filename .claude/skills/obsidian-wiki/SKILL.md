---
name: obsidian-wiki-curator
description: Maintains a personal "second brain" Obsidian vault — a zero-loss knowledge graph of generated concept/entity pages cross-linked with wikilinks, governed by a CLAUDE.md schema at the vault root. Use to (1) ingest a note/source/pasted text into the knowledge graph ("ingest this", "add this to my notes/wiki"), (2) integrate a raw note the user wrote by hand directly in the wiki ("I added something to this page, integrate it"), (3) find and integrate every unintegrated manual change at once ("identify all changes and add them"), (4) query the wiki and optionally save the answer as a page, or (5) lint for contradictions, orphan pages, broken links, missing cross-references. Works with any vault of this kind, not a specific one — reads whatever CLAUDE.md it finds in the working folder as source of truth, and offers to bootstrap one from references/methodology.md if none exists.
---
 
# Obsidian Wiki Curator
 
## Before doing anything
 
1. Check the working folder for a `CLAUDE.md` and a wiki-pages folder (commonly `wiki/`, with
   an `index.md` and a `log.md`). If neither is mounted/accessible, ask the user to connect
   the vault folder.
2. **If `CLAUDE.md` exists: read it in full and treat it as the source of truth.** It defines
   this vault's exact folder names, tag conventions, page templates, and any established
   precedents — follow it over the generic guidance below wherever they differ.
3. **If no `CLAUDE.md` exists yet:** this is a new vault. Read `references/methodology.md`,
   discuss with the user how they want to adapt it (domain areas, language, folder names), and
   write a vault-specific `CLAUDE.md` together before doing any content work.
4. For a query specifically: read `index.md` next to find relevant pages before opening
   anything else — never scan the whole vault up front.
## The three ways content enters the wiki
 
All three end in the same underlying ingest work (zero-loss reformatting, index update, log
entry) — they just differ in where the raw material comes from:
 
- **Pasted in chat**: user gives you text/a source directly and asks you to ingest it. Discuss
  the best place(s) for it in the graph, then write it in.
- **Written directly into the wiki**: user tells you they added/edited a specific page by hand
  and asks you to integrate it. If the vault is git-tracked, `git diff` on that file (or just read the
  whole file if it's new/untracked) to see exactly what's raw; otherwise just re-read the page
  and use judgment about what's new. Reformat it in place to zero-loss standard.
- **"Identify all changes"**: user wants everything they've touched found and integrated
  without naming files. This requires git (see below) — if the vault isn't git-tracked yet,
  offer to set it up rather than guessing at what changed.
See `references/methodology.md` for the full write-up of the git-tracking setup (`.gitignore`
for attachments/UI-state, the "clean tree = fully integrated" invariant, and how to distinguish
a real new-content diff from a trivial edit) and the general zero-loss/linking conventions —
skip that file entirely if this vault's own `CLAUDE.md` already covers it, which it usually will
once set up.
 
## Query and lint
 
**Query**: read the index, open only the relevant pages, answer with citations to specific
pages/sections (link to the exact heading when the reference is about part of a page, not all
of it — this convention matters enough that it's worth getting right even if the vault's
`CLAUDE.md` doesn't spell it out explicitly). Offer to save a genuinely valuable answer as a
page; don't do this automatically for every answer.
 
**Lint** (on request): check for contradictions between pages, stale claims superseded by
newer content, orphan pages with no incoming links, concepts mentioned repeatedly but missing
their own page, and missing cross-references. Run `scripts/scan_broken_links.py, passing the vault root 
(and content folder name if not "wiki")` before and after any batch of edits and compare the "Outside log.md" count (or
equivalent changelog-file name) to the last documented baseline — a vault accumulates a handful
of permanent, documented false positives over time (illustrative syntax in its own schema file,
genuinely missing source images, etc.); investigate anything *new*, don't assume either a zero
or a nonzero count means what it looks like without checking. Never guess-fix a broken
link/embed by pattern-matching a filename to something that merely looks similar — verify the
candidate file is actually owned by/relevant to the page in question first, since generic
filenames (e.g. sequential export names like `image12.png`) can collide across completely
unrelated content.
 
## Non-negotiable defaults (fall back on these only where the vault's own CLAUDE.md is silent)
 
- Zero-loss: a generated page is the source content in full, reformatted — never a summary.
- Section-anchor links whenever a reference concerns part of a page, not the whole thing.
- The changelog/log file is append-only — never edit or delete old entries, even ones that
  later reference deleted pages; that's expected history, not a bug.
- Always commit (if git-tracked) after finishing wiki changes — a clean tree is what makes
  "identify all changes" possible without extra bookkeeping.