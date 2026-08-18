# Genealogy Site — Backlog

_Last updated: 2026-08-18_

## TODO: Add birthplace locations to every person node

User feedback: the location data (where each ancestor was *born*, not just buried) is
the most interesting part of the tree. Several nodes currently show birth/death + burial
but **no birthplace**, and several show only a country/region with no specific town.

### Research targets

**genealogy.html (Bates/Ryan/Madsen tree)**
- [x] Leman Bronson → Middlebury, New Haven, CT (WikiTree)
- [x] Halmagh John Van Wagoner → Bergen Co., NJ (Find a Grave)
- [x] Edwin Ruthven Bronson → Mentor, Lake, OH (WikiTree)
- [x] John Halmagh Van Wagoner → Pompton Plains, Morris, NJ (WikiTree)
- [ ] Peter Henry Madsen — has "Denmark" but no specific town (confirmed Danish immigrant)
- [ ] William Enos Bench — has "Axtell, UT" but verify birth vs. residence

**tara-family.html (Wasden/Quarnberg/Candland tree)**
- [x] Henry Maiben → Brighton, East Sussex, England (Find a Grave)
- [x] Sanford Holman → Nauvoo, Hancock, IL (Find a Grave)
- [ ] John Harvey Partridge — no birth place in Find a Grave; died Goshen, UT 1932
- [ ] David Lester Holman — family record says Fountain Green, UT (tara line 656); add to node
- [ ] Richard Robins — England only, no town (Find a Grave lists no birth place)
- [x] William Johnson — "Leigh, Worcestershire, England" (verified)
- [ ] Hans Nielson — sources conflict: Sweden (family lore) vs. Denmark; left as "Sweden"
- [x] Hezekiah Partridge → Worthington, Hampshire, MA (Find a Grave)
- [x] Jonathan Holman Jr. — "Templeton, MA" (verified)
- [x] David LeBaron — "LeRoy, Genesee County, NY" (verified)
- [x] James Allred — "Bedford County, TN" (verified)

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
