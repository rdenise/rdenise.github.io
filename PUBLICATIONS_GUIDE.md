# Publication Page Formatting Guide

This document explains how to format publication entries to match the timeline-style layout with icons.

## Basic Structure

Each publication file in `_publications/` should have the following frontmatter:

```yaml
---
title: "Your Paper Title"
collection: publications
permalink: /publication/YYYY-MM-DD-url-slug
date: YYYY-MM-DD
venue: 'Journal Name'
paperurl: 'https://link-to-paper'
citation: ' Authors, <b>Your Paper Title.</b> <i>Journal Name</i>, YYYY.'
---
```

## Citation Formatting

The citation field should follow this format:
- **Authors**: Plain text, separated by commas
- **Title**: Wrapped in `<b>` tags for bold
- **Venue**: Wrapped in `<i>` tags for italics
- **Year**: Plain text at the end

Example:
```
citation: ' J. Smith,  M. Doe, <b>Amazing Research Title.</b> <i>Nature</i>, 2023.'
```

## Adding Supplementary Links

You can add the following optional fields to display icons after each publication:

### GitHub Repository
```yaml
githuburl: 'https://github.com/username/repo'
```
or
```yaml
code: 'https://github.com/username/repo'
```

### Open Access Link
```yaml
oa_paperurl: 'https://open-access-link'
```

### OSF Link
```yaml
osfurl: 'https://osf.io/xxxxx/'
```

### Related Resources
```yaml
relatedurl: 'https://related-resource-link'
```

## Complete Example

```yaml
---
title: "MacSyFinder v2: Improved modelling and search engine to identify molecular systems in genomes"
collection: publications
permalink: /publication/2023-01-01-macsyfinder-v2
date: 2023-01-01
venue: 'Peer Community Journal'
paperurl: 'https://doi.org/10.24072/pcjournal.285'
githuburl: 'https://github.com/gem-pasteur/macsyfinder'
citation: ' B. Néron,  R. Denise,  C. Coluzzi,  M. Touchon,  E. Rocha,  S. Abby, <b>MacSyFinder v2: Improved modelling and search engine to identify molecular systems in genomes.</b> <i>Peer Community Journal</i>, 2023.'
---
```

## Display Icons

The following icons will appear automatically when you add the corresponding URL fields:

- 🔗 Link icon: Always appears for `paperurl`
- <i class="fab fa-github"></i> GitHub icon: Appears when `githuburl` or `code` is present
- 🔓 Open Access icon: Appears when `oa_paperurl` is present
- OSF icon: Appears when `osfurl` is present
- ∼ Tilde symbol: Appears when `relatedurl` is present

## Running the Update Script

If you need to update citation formatting across all publications:

```bash
python3 update_citations.py
```

This will:
- Add `<i>` tags around venue names
- Ensure consistent formatting across all publications
