# Genealogy Site — Backlog

_Last updated: 2026-08-18_

## TODO: Add birthplace locations to every person node

User feedback: the location data (where each ancestor was *born*, not just buried) is
the most interesting part of the tree. Several nodes currently show birth/death + burial
but **no birthplace**, and several show only a country/region with no specific town.

### Research targets

**genealogy.html (Bates/Ryan/Madsen tree)**
- [ ] Leman Bronson — no birthplace (only "UT" burial context)
- [ ] Halmagh John Van Wagoner — no birthplace
- [ ] Edwin Ruthven Bronson — no birthplace
- [ ] John Halmagh Van Wagoner — no birthplace
- [ ] Peter Henry Madsen — has "Denmark" but no specific town (confirmed Danish immigrant)
- [ ] William Enos Bench — has "Axtell, UT" but verify birth vs. residence

**tara-family.html (Wasden/Quarnberg/Candland tree)**
- [ ] Henry Maiben — no birthplace (Salt Lake City burial only)
- [ ] Sanford Holman — no birthplace
- [ ] John Harvey Partridge — no birthplace
- [ ] David Lester Holman — no birthplace
- [ ] Richard Robins — "England" only, no town
- [ ] William Johnson — "Leigh, Worcestershire, England" (have it — verify)
- [ ] Hans Nielson — "Sweden" only, no town/parish
- [ ] Hezekiah Partridge — no specific birthplace
- [ ] Jonathan Holman Jr. — "Templeton, MA" (have it — verify)
- [ ] David LeBaron — "LeRoy, Genesee County, NY" (have it — verify)
- [ ] James Allred — "Bedford County, TN" (have it — verify)

### Deliberately left location-private (modern living/descendant lines)
Gene & Carolyn Bates, Mike & Cindy Bates, Dave Bates, Cliff & Tara Bates,
Jarred Bates, Ethan Bates, Mark Lloyd Wasden, Meghan Wasden, Tara Ann Wasden Bates.

### Sources
- Find a Grave memorial "born in" fields (already cached under
  `~/.hermes/profiles/atlas/cache/web/www.findagrave.com-*.md`)
- Obituaries (Legacy.com, Salt Lake Tribune, Larkin Mortuary)
- FamilySearch (where accessible)

### Workflow
1. Pull each missing birthplace from Find a Grave "Born:" field or obituary.
2. Add to the node `<span class="meta">` line as `· <BirthPlace>` (consistent with
   existing nodes that already show `· <place>`).
3. Re-validate HTML (python html.parser script).
4. Commit + `git push origin main` from `~/Projects/batesfam.net`.
