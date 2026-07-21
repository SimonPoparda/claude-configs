# Zero-loss personal wiki methodology
 
Generic pattern this skill implements (based on https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
If a vault already has its own `CLAUDE.md`, that file overrides everything below where they
differ — this is a fallback/bootstrap template, not a spec to enforce.
 
## Two-layer architecture
 
- **Layer 1 — generated pages** (commonly `wiki/`): markdown pages Claude owns, plus an
  `index.md` (catalog, updated on every change) and an append-only `log.md` (chronological
  record of every ingest/query/lint, one entry per `## [YYYY-MM-DD] type | title`, never edited
  retroactively). Typical subfolders: `concepts/` (ideas, technologies, topics), `entities/`
  (people, projects, tools-as-things), `syntheses/` (saved answers to valuable questions),
  and an attachments folder for embedded images (usually excluded from git — see below).
- **Layer 2 — schema** (`CLAUDE.md` at the vault root): the rules both of you co-maintain.
  Propose edits to it whenever a new lasting convention emerges; log the change in `log.md`
  as a `schema-update` entry.
## Zero-loss rule (the core principle)
 
A generated page is the source content in full, reformatted and integrated into the graph —
never a summary. Reformatting, grouping into sections, adding frontmatter, and adding
`[[wikilinks]]` where the text already mentions other concepts is fine; dropping facts, steps,
numbers, or examples is not. If a source is long and covers several loosely-related topics,
split it into multiple pages (one per topic), each carrying 100% of the content on that topic
— not an excerpt of it.
 
## Linking conventions
 
- File name = the page's own readable title (no kebab-case), so graph view shows clean labels.
- Link with `[[wikilinks]]`. When a reference is about a specific section of a page rather
  than the whole page, link directly to that section (page name, `#`, then the exact heading
  text, inside double brackets, optionally piped with `|display text`) instead of the whole
  page — do this for every such reference, not just occasionally.
- For inflected languages, use a piped link to keep the link target exact while the visible
  text takes whatever grammatical form fits the sentence.
## The three operations
 
1. **Ingest** — adding a source. Discuss the topic split with the user first unless they
   explicitly ask for a batch/no-discussion ingest. Write full zero-loss content into the
   appropriate page(s), update the index, append a `log.md` entry (include any split/editorial
   decisions directly in that entry — don't create separate "pointer" pages for this, it just
   duplicates what the log already records). Flag contradictions with existing pages explicitly
   instead of silently overwriting.
2. **Query** — read the index to find relevant pages, open only those, answer with citations
   to the specific pages/sections. Offer (don't force) saving a valuable answer as a synthesis
   page.
3. **Lint** — on request, check for contradictions, stale claims, orphan pages, missing
   cross-references, and repeatedly-mentioned concepts that deserve their own page. Run
   `scripts/scan_broken_links.py` before and after any batch of edits and compare counts.
   Propose actions; only execute the non-obvious ones after the user approves.
## Detecting manual edits with git (for vaults that support writing notes directly into the wiki)
 
Some users want to jot raw notes straight into the wiki folder (new page, or an addition to an
existing one) instead of only pasting text into chat. To support "identify everything I changed
and integrate it" without asking the user to enumerate files, track the vault with git:
 
- `git init` at the vault root once; `.gitignore` the attachments/binary folder and noisy
  Obsidian UI-state files (workspace.json changes on every app open/close and carries no
  content); commit a baseline of the current state.
- **Invariant: a clean working tree means everything is already integrated.** Always commit
  after finishing any change to the wiki. This makes `git status --porcelain` at the start of
  any request an unambiguous list of the user's own not-yet-integrated edits.
- Three ways content enters the wiki, all ending in the same Ingest procedure above:
  1. User pastes text/a note in chat and asks to ingest it — no git involved.
  2. User edits/creates a page directly in the wiki and names it — read that file (`git diff`
     for an existing page, the whole file for a new untracked one) to see exactly what's raw,
     then integrate it in place.
  3. User asks to find and integrate *everything* changed — run `git status --porcelain`,
     process every touched file under the wiki folder, commit at the end.
- Not every diff needs the full Ingest treatment — a one-word typo fix is just an edit; a
  paragraph of new, unformatted prose is a real ingest. Use judgment, and when genuinely
  unsure, ask.
- This works the same regardless of which device produced the edit (desktop, mobile, etc.) —
  git only observes files on disk, not who wrote them. It requires whatever sync mechanism
  already keeps the vault consistent across devices (Obsidian Sync, iCloud, Syncthing,
  Dropbox, ...) to have actually delivered the edit into this folder first.