---
schema_version: 2
id: uber-mcp-gateway-31398518-002
title: Two planes
background_image: images/network.svg
source_url: https://blog.bytebytego.com/p/how-uber-built-a-gateway-for-ai-agents
source_file: null
source_title: How Uber Built A Gateway For AI Agents To Access Tools
source_type: article
source_locator: 'Section: How the Uber MCP Gateway is Designed'
sort_order: 2
language: en
---

Uber separates two jobs:

- The **control plane**, including the Registry, keeps catalog and configuration information.
- The **data plane**, including the Proxy Gateway, handles live requests.

Agents and owners can discover tools through the catalog while actual calls take a controlled execution path. This keeps discovery, configuration and runtime handling connected without making them the same responsibility.

![Uber’s MCP Registry lists discoverable servers and tools as the control plane.](images/source-03.webp)

*Source: ByteByteGo’s article; credited to Uber Engineering in the article. Tap to enlarge; the complete figure is preserved.*
