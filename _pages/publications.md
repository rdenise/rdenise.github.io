---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  You can also find a complete list of my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.
{% endif %}

{% include base_path %}

<div class="publications">

  <h2>Research Articles</h2>
  <ul>
    {% assign research_pubs = site.publications | where: "publication_type", "research" | reverse %}
    {% for post in research_pubs %}
      {% include archive-single-cv.html %}
    {% endfor %}
  </ul>

  <h2>Review Papers</h2>
  <ul>
    {% assign review_pubs = site.publications | where: "publication_type", "review" | reverse %}
    {% for post in review_pubs %}
      {% include archive-single-cv.html %}
    {% endfor %}
  </ul>

  <h2>Book Chapters</h2>
  <ul>
    {% assign book_pubs = site.publications | where: "publication_type", "book_chapter" | reverse %}
    {% for post in book_pubs %}
      {% include archive-single-cv.html %}
    {% endfor %}
  </ul>

  <h2>PhD Thesis</h2>
  <ul>
    {% assign thesis_pubs = site.publications | where: "publication_type", "thesis" %}
    {% for post in thesis_pubs %}
      {% include archive-single-cv.html %}
    {% endfor %}
  </ul>

</div>
