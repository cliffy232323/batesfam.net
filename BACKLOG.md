# Genealogy Site — Backlog

_Last updated: 2026-08-18_

## TODO: Add birthplace locations to every person node

User feedback: the location data (where each ancestor was *born*, not just buried) is
the most interesting part of the tree. Several nodes currently show birth/death + burial
but **no birthplace**, and several show only a country/region with no specific town.

### Research targets

**bates-family-tree.html (Bates/Ryan/Madsen tree)**
- [x] Leman Bronson → Middlebury, New Haven, CT (WikiTree)
- [x] Halmagh John Van Wagoner → Bergen Co., NJ (Find a Grave)
- [x] Edwin Ruthven Bronson → Mentor, Lake, OH (WikiTree)
- [x] John Halmagh Van Wagoner → Pompton Plains, Morris, NJ (WikiTree)
- [ ] Peter Henry Madsen — has "Denmark" but no specific town (confirmed Danish immigrant)
- [ ] William Enos Bench — has "Axtell, UT" but verify birth vs. residence

**wasden-family-tree.html (Wasden/Quarnberg/Candland tree)**
- [x] Henry Maiben → Brighton, East Sussex, England (Find a Grave)
- [x] Sanford Holman → Nauvoo, Hancock, IL (Find a Grave)
- [x] David Lester Holman → Fountain Green, UT (FamilySearch + tara line 656 note)
- [x] John Harvey Partridge → Goshen, UT (death/birth place per census)
- [x] Richard Robins → Deerhurst, Gloucestershire, England (Ancestry/FamilySearch)
- [x] Hans Nielson → Gotland, Sweden (daughter Christina b. Gotlands län)
- [ ] Peter Henry Madsen — Denmark only, no town (Goshen 1880 census; born ~1860 Denmark)

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
