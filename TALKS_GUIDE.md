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

## New Layout Features

The talks page now features:
- **Title**: Linked to a detail page for the talk/poster (where you can add abstract, slides, etc.)
- **Venue**: Displayed below the title with the type (Talk/Poster)
- **Location**: Displayed in a separate column on the right side
- **Conference Link**: Optional link to the conference website displayed below the venue
- **Year**: Shown in the timeline bubble (no full date displayed in main content)

## Talk Types

Specify the type of presentation:
- `Talk`: For oral presentations
- `Poster`: For poster presentations
- `Tutorial`: For tutorial sessions
- `Workshop`: For workshop presentations

## Adding Links

### Conference Website URL
```yaml
conferenceurl: 'https://conference-website.org'
```
This will display a "Conference website" link with an external link icon below the venue.

### Talk URL (Specific Session/Abstract Page)
```yaml
talkurl: 'https://conference-website/session/your-talk'
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
conferenceurl: 'https://jobim2018.sciencesconf.org/'
slidesurl: '/files/slides/2018-JOBIM-talk.pdf'
videourl: 'https://youtube.com/watch?v=example'
---

# Abstract

Add your talk abstract here. This will be displayed on the individual talk page.

## Additional Information

You can add any additional information about the talk here, such as:
- Key points
- Related publications
- Acknowledgments
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
conferenceurl: 'https://isba10.ut.ee/'
posterurl: '/files/posters/2023-ISBA-poster.pdf'
---

# Poster Details

Add poster abstract and details here.
```

## Display Icons

The following icons will appear automatically when you add the corresponding URL fields:

- 🔗 Link icon: Appears when `talkurl` is present (link to specific talk/session page)
- 📄 PDF icon: Appears when `slidesurl` is present (link to slides)
- 🖼️ Image icon: Appears when `posterurl` is present (link to poster PDF)
- 🎥 Video icon: Appears when `videourl` is present (link to video recording)
- 🔗 "Conference website" link: Appears when `conferenceurl` is present (below venue name)

## Layout Display

The talks will be displayed in this format:

```
[YYYY]  **Title** (linked to detail page)                    Location
        Type at *Venue*
        🔗 Conference website
        [icons for materials]
```

Example:
```
2018    **Co-option of complex molecular systems**          Marseille, France
        Talk at *JOBIM*
        🔗 Conference website
        📄 🎥
```

## Creating Detail Pages

Each talk file should contain content that will be displayed on its individual page:

```markdown
---
[frontmatter as shown above]
---

# Abstract

Your talk or poster abstract goes here.

## Slides

[Embed slides if desired]

## Key Points

- Point 1
- Point 2
- Point 3
```

## File Organization

Store your supplementary files in organized directories:
- Slides: `/files/slides/`
- Posters: `/files/posters/`
- Other materials: `/files/talks/`

## Tips

1. Keep file names consistent and descriptive
2. Use YYYY-MM-DD prefix for files to make them easy to sort
3. Add `conferenceurl` for official conference websites
4. Fill in the content of each talk file with abstract, slides, or other details
5. The title will automatically link to this detail page
6. Use the location field for "City, Country" format for best display
