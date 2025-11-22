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
  <ul>
    {% assign reversed_pubs = site.publications | reverse %}
    {% for post in reversed_pubs %}
      {% include archive-single-cv.html last_item=forloop.last %}
    {% endfor %}
  </ul>
</div>
