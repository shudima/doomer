---
schema_version: 2
id: uber-mcp-gateway-31398518-001
title: Tools reach systems
background_image: images/network.svg
source_url: https://blog.bytebytego.com/p/how-uber-built-a-gateway-for-ai-agents
source_file: null
source_title: How Uber Built A Gateway For AI Agents To Access Tools
source_type: article
source_locator: 'Section: Why AI Agents Need Tools; The Role of MCP at Uber'
sort_order: 1
language: en
---

An agent needs tools to inspect a deployment, search internal logs or query a business system. A language model alone cannot reach those systems.

**Model Context Protocol**, or MCP, standardizes how clients discover tool descriptions and call servers. Uber uses that common interface across its tool ecosystem. The surrounding gateway still has to provide useful descriptions, access checks and reliable execution.
