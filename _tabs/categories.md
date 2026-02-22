---
layout: categories
title: Build Sheet
permalink: /categories/
icon: fas fa-stream
order: 1
---
<ul class="list-group list-group-flush">
  {% for category in site.categories %}
    {% assign name = category | first %}
    {% assign posts = category | last %}
    {% assign slug = name | downcase | strip %}

    <li class="list-group-item d-flex justify-content-between align-items-center">
      <a href="{{ site.baseurl }}/categories/{{ name | slugify }}/">
        {% if slug contains 'engine' %}
          <i class="fas fa-cogs fa-fw"></i>
        {% elsif slug contains 'interior' %}
          <i class="fas fa-couch fa-fw"></i>
        {% elsif slug contains 'exterior' %}
          <i class="fas fa-car fa-fw"></i>
        {% elsif slug contains 'mechanical' %}
          <i class="fas fa-wrench fa-fw"></i>
        {% elsif slug contains 'turbo' %}
          <i class="fas fa-wind fa-fw"></i>
        {% elsif slug contains 'fuel' %}
          <i class="fas fa-gas-pump fa-fw"></i>
        {% else %}
          <i class="fas fa-folder-open fa-fw"></i>
        {% endif %}
        <span class="ml-2">{{ name }}</span>
      </a>
      <span class="badge badge-pill badge-secondary">{{ posts.size }}</span>
    </li>
  {% endfor %}
</ul>

<hr>
<p>System Check: {{ site.categories.size }} categories found.</p>
