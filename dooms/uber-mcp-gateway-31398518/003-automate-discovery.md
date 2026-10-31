---
schema_version: 2
id: uber-mcp-gateway-31398518-003
title: Automate discovery
background_image: images/network.svg
source_url: https://blog.bytebytego.com/p/how-uber-built-a-gateway-for-ai-agents
source_file: null
source_title: How Uber Built A Gateway For AI Agents To Access Tools
source_type: article
source_locator: 'Section: How Tools Are Discovered'
sort_order: 3
language: en
---

Registering every tool by hand would make a large catalog hard to maintain. Uber’s **AutoCrawler**, powered by Cadence, discovers existing capabilities.

It translates API contracts into tool schemas and uses an LLM to improve descriptions. Native MCP servers can announce themselves through heartbeats. Discovery supplies the catalog; owners still review and enable tools before agents can use them.
