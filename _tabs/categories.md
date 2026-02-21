---
layout: page
title: Build Process
permalink: /categories/
icon: fas fa-stream
order: 1
---

### Raw Category Debug List:
<ul>
  {% for category in site.categories %}
    <li>{{ category | first }} ({{ category | last | size }})</li>
  {% endfor %}
</ul>