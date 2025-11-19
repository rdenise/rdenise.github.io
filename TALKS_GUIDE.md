# Talks and Presentations Formatting Guide

This document explains how to format talk entries to match the timeline-style layout with icons.

## Basic Structure

Each talk file in `_talks/` should have the following frontmatter:

```yaml
---
title: "Your Talk or Poster Title"
collection: talks
type: "Talk"  # or "Poster"
permalink: /talks/DD/MM/YYYY-url-slug
venue: "Conference Name"
date: DD/MM/YYYY
location: "City, Country"
---
```

## Talk Types

Specify the type of presentation:
- `Talk`: For oral presentations
- `Poster`: For poster presentations
- `Tutorial`: For tutorial sessions
- `Workshop`: For workshop presentations

## Adding Supplementary Links

You can add the following optional fields to display icons after each talk:

### Talk URL (Conference/Event Page)
```yaml
talkurl: 'https://conference-website/session'
```

### Slides URL
```yaml
slidesurl: 'https://link-to-slides.pdf'
```
or
```yaml
slidesurl: '/files/slides/2023-talk-slides.pdf'
```

### Poster URL
```yaml
posterurl: 'https://link-to-poster.pdf'
```
or
```yaml
posterurl: '/files/posters/2023-poster.pdf'
```

### Video Recording URL
```yaml
videourl: 'https://youtube.com/watch?v=xxxxx'
```

## Complete Example

```yaml
---
title: "Co-option of complex molecular systems in bacterial and archaeal membranes"
collection: talks
type: "Talk"
permalink: /talks/05/07/2018-talk-1
venue: "JOBIM"
date: 05/07/2018
location: "Marseille, France"
talkurl: 'https://jobim2018.sciencesconf.org/'
slidesurl: '/files/slides/2018-JOBIM-talk.pdf'
videourl: 'https://youtube.com/watch?v=example'
---
```

## Example Poster

```yaml
---
title: "Diversity of bacteriophages in the ancient human microbiome"
collection: talks
type: "Poster"
permalink: /talks/13/07/2023-poster-10
venue: "ISBA - New Horizons in Biomolecular Archaeology"
date: 13/07/2023
location: "Tartu, Estonia"
posterurl: '/files/posters/2023-ISBA-poster.pdf'
---
```

## Display Icons

The following icons will appear automatically when you add the corresponding URL fields:

- 🔗 Link icon: Appears when `talkurl` is present (link to conference/event)
- 📄 PDF icon: Appears when `slidesurl` is present (link to slides)
- 🖼️ Image icon: Appears when `posterurl` is present (link to poster PDF)
- 🎥 Video icon: Appears when `videourl` is present (link to video recording)

## Formatting Guidelines

1. **Title**: Will be displayed in bold
2. **Type**: Automatically added (Talk, Poster, etc.)
3. **Venue**: Will be displayed in italics
4. **Location**: Plain text, separated by comma
5. **Date**: Displayed as provided in DD/MM/YYYY format

The format will be:
```
<bold>Title</bold>, Type, <italic>Venue</italic>, Location, Date
```

Example output:
```
**Co-option of complex molecular systems in bacterial and archaeal membranes**, Talk, *JOBIM*, Marseille, France, 05/07/2018
```

## File Organization

Store your supplementary files in organized directories:
- Slides: `/files/slides/`
- Posters: `/files/posters/`
- Other materials: `/files/talks/`

## Tips

1. Keep file names consistent and descriptive
2. Use YYYY-MM-DD prefix for files to make them easy to sort
3. Add all relevant URLs to make it easy for visitors to access your materials
4. Venue names should be the official conference/event name
