#!/usr/bin/env python3
"""
Scan an Obsidian vault for broken [[wikilinks]] and ![[embeds]].
 
Usage:
    python3 scan_broken_links.py [vault_root] [content_dir]
 
vault_root defaults to the current directory (must contain CLAUDE.md and a
wiki-pages folder). content_dir is the folder holding the generated pages
to scan for *outgoing* links (defaults to "wiki") - only files in there and
CLAUDE.md itself are scanned as "active content"; everything else in the
vault is only used to build the set of valid link/embed targets.
 
If the vault has an append-only changelog file (commonly wiki/log.md) that
intentionally keeps references to since-deleted pages, exclude it from the
"is this clean" judgment call the same way - report its broken links
separately rather than mixing them into the active-content count.
"""
import re
import os
import sys
 
vault_root = sys.argv[1] if len(sys.argv) > 1 else "."
content_dir_name = sys.argv[2] if len(sys.argv) > 2 else "wiki"
 
all_basenames = set()
media_basenames = set()
for root, dirs, files in os.walk(vault_root):
    if "/.git" in root or "/.obsidian" in root:
        continue
    for fn in files:
        all_basenames.add(fn)
        all_basenames.add(os.path.splitext(fn)[0])
        if not fn.endswith(".md"):
            media_basenames.add(fn)
 
scan_files = []
content_dir = os.path.join(vault_root, content_dir_name)
for root, dirs, files in os.walk(content_dir):
    for fn in files:
        if fn.endswith(".md"):
            scan_files.append(os.path.join(root, fn))
claude_md = os.path.join(vault_root, "CLAUDE.md")
if os.path.exists(claude_md):
    scan_files.append(claude_md)
 
link_re = re.compile(r'(?<!!)\[\[([^\]|#]+)')
embed_re = re.compile(r'!\[\[([^\]|#]+)')
 
broken = []
for f in scan_files:
    with open(f, encoding="utf-8") as fh:
        text = fh.read()
    for m in link_re.finditer(text):
        target = m.group(1).strip()
        if target not in all_basenames:
            broken.append((f, "link", target))
    for m in embed_re.finditer(text):
        target = m.group(1).strip()
        if target not in media_basenames and target not in all_basenames:
            broken.append((f, "embed", target))
 
print(f"Total broken: {len(broken)}")
changelog_hits = [b for b in broken if os.path.basename(b[0]) == "log.md"]
other_hits = [b for b in broken if os.path.basename(b[0]) != "log.md"]
print(f"Outside log.md: {len(other_hits)} <- judge cleanliness by this number")
if changelog_hits:
    print(f"Inside log.md: {len(changelog_hits)} <- expected to grow over time if the "
          f"changelog is append-only; not a bug by itself")
for f, kind, t in broken:
    print(f"  [{kind}] {f} -> {t}")