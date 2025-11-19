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
{% for post in site.publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}

</div>
