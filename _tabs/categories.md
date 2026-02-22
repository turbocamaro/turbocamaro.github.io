---
layout: categories
title: Build Sheet
permalink: /categories/
icon: fas fa-stream
order: 1
---
<div class="flex-grow-1">
  <ul class="list-group list-group-flush">
    {% assign sorted_categories = site.categories | sort %}
    {% for category in sorted_categories %}
      {% comment %} Get the name and strip any hidden spaces {% endcomment %}
      {% assign category_name = category | first | strip %}
      {% assign slug = category_name | downcase %}
      
      <li class="list-group-item d-flex justify-content-between align-items-center">
        <a href="{{ site.baseurl }}/categories/{{ category_name | slugify }}/" class="ml-1 text-decoration-none">
          
          {% if slug == "engine" %}
            <i class="fas fa-cogs fa-fw mr-2"></i>
          {% elsif slug == "interior" %}
            <i class="fas fa-couch fa-fw mr-2"></i>
          {% elsif slug == "exterior" %}
            <i class="fas fa-car fa-fw mr-2"></i>
          {% elsif slug == "mechanical" %}
            <i class="fas fa-wrench fa-fw mr-2"></i>
          {% elsif slug contains "turbo" %}
            <i class="fas fa-wind fa-fw mr-2"></i>
          {% elsif slug contains "fuel" %}
            <i class="fas fa-gas-pump fa-fw mr-2"></i>
          {% else %}
            {% comment %} This folder stays as a fallback {% endcomment %}
            <i class="fas fa-folder-open fa-fw mr-2"></i>
          {% endif %}
          
          {{ category_name }}
        </a>
        <span class="badge badge-pill badge-secondary">{{ category | last | size }}</span>
      </li>
    {% endfor %}
  </ul>
</div>

{% comment %} 
DEBUG SECTION: If you still see folders, look at the text below on your live site. 
It will show exactly what 'slug' is being generated.
{% endcomment %}
<hr>
<small class="text-muted">Debug - System sees: {% for category in site.categories %}[{{ category | first | downcase }}] {% endfor %}</small>
