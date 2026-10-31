---
schema_version: 2
id: design-patterns-in-machine-learning-code-and-systems-40f8e1de-012
title: A reverse proxy provides one public entrance
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/design-patterns/
source_file: null
source_title: Design Patterns in Machine Learning Code and Systems
source_type: article
source_locator: 'Section: Design patterns in systems — reverse proxy'
sort_order: 14
language: en
---

Horizontal scaling creates several model-serving machines, but clients can still use one address. A reverse proxy receives requests and distributes them among the backends.

Yan distinguishes the broader proxy role from load balancing alone. Depending on the setup, the proxy can also cache responses, limit direct backend exposure and terminate encrypted connections, centralizing responsibilities that individual model servers need not each implement.

![Using a reverse proxy to distribute incoming requests to multiple backend servers](images/source-03.webp)

*Source: Eugene Yan’s article; underlying paper credits remain in the figure and linked source. Tap to enlarge; the complete figure is preserved.*
