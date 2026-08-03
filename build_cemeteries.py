#!/usr/bin/env python3
"""Inject per-person GPS links into cemeteries.html from graves.json.

graves.json is the synced Google Sheet data (run fetch_graves.py first).
For each <li> in a .cemetery card, match by the card's <h2> cemetery name
and the <span class="b-name"> person name to a graves.json row, and append a
"GPS location ↗" link (the row's maps/directions URL). Re-run after the sheet
changes to refresh.
"""
import json
import re
import os

HERE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(HERE, "cemeteries.html")
JSON = os.path.join(HERE, "graves.json")

with open(JSON, encoding="utf-8") as f:
    graves = json.load(f)

by_key = {}
for g in graves:
    key = (g.get("cemetery", "") + "|" + g.get("name", "") + "|" + g.get("relationship", "")).lower()
    by_key[key] = g

with open(HTML, encoding="utf-8") as f:
    html = f.read()

# Strip any previously-injected gps-links so re-runs are idempotent
html = re.sub(r'\s*<a class="gps-link"[^>]*>GPS location ↗</a>', "", html)

# Process each cemetery article
def inject(card):
    h2 = re.search(r"<h2>(.*?)</h2>", card)
    if not h2:
        return card
    cem = h2.group(1).strip()

    def repl_li(li):
        nm = re.search(r'class="b-name">(.*?)<', li)
        if not nm:
            return li
        name = nm.group(1).strip()
        rl = re.search(r'class="b-rel">(.*?)<', li)
        rel = rl.group(1).strip() if rl else ""
        g = by_key.get((cem + "|" + name + "|" + rel).lower())
        if not g or not g.get("maps"):
            return li
        link = (f'<a class="gps-link" href="{g["maps"]}" target="_blank" '
                f'rel="noopener">GPS location ↗</a>')
        return li.replace("</li>", link + "</li>", 1)

    return re.sub(r"<li>.*?</li>", lambda m: repl_li(m.group(0)), card, flags=re.S)

new_html = re.sub(
    r'<article class="cemetery".*?</article>',
    lambda m: inject(m.group(0)),
    html,
    flags=re.S,
)

with open(HTML, "w", encoding="utf-8") as f:
    f.write(new_html)

added = new_html.count('class="gps-link"')
print(f"Injected {added} GPS links from graves.json")
