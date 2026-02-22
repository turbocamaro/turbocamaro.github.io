---
layout: categories
title: Build Sheet
permalink: /categories/
icon: fas fa-stream
order: 1
---
<div class="post-content">
  <div class="categories-list">
    {% assign sorted_categories = site.categories | sort %}
    {% for category in sorted_categories %}
      {% assign category_name = category | first %}
      {% assign posts = category | last %}
      {% assign slug = category_name | downcase %}

      <div class="d-flex justify-content-between align-items-center py-2 border-bottom">
        <a href="{{ site.baseurl }}/categories/{{ category_name | slugify }}/" class="text-decoration-none d-flex align-items-center">
          <span class="mr-3 text-muted" style="width: 30px; text-align: center;">
            {% if slug contains "engine" %}
              <i class="fas fa-cogs fa-fw"></i>
            {% elsif slug contains "interior" %}
              <i class="fas fa-couch fa-fw"></i>
            {% elsif slug contains "exterior" %}
              <i class="fas fa-car fa-fw"></i>
            {% elsif slug contains "mechanical" %}
              <i class="fas fa-wrench fa-fw"></i>
            {% elsif slug contains "turbo" %}
              <i class="fas fa-wind fa-fw"></i>
            {% elsif slug contains "fuel" %}
              <i class="fas fa-gas-pump fa-fw"></i>
            {% else %}
              <i class="fas fa-folder-open fa-fw"></i>
            {% endif %}
          </span>
          <span class="h5 mb-0">{{ category_name }}</span>
        </a>
        <span class="badge badge-pill bg-secondary text-white">{{ posts.size }}</span>
      </div>
    {% endfor %}
  </div>
</div>
