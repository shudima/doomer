---
schema_version: 2
id: uber-mcp-gateway-31398518-005
title: Translate every call
background_image: images/network.svg
source_url: https://blog.bytebytego.com/p/how-uber-built-a-gateway-for-ai-agents
source_file: null
source_title: How Uber Built A Gateway For AI Agents To Access Tools
source_type: article
source_locator: 'Section: How Uber’s MCP Gateway Works'
sort_order: 5
language: en
---

A shared MCP interface can sit in front of services that speak different protocols. Uber’s gateway translates requests and responses for HTTP, gRPC and TChannel backends.

Periodically refreshed mappings create virtual MCP endpoints for those capabilities. An agent uses the common tool interface while the gateway handles the service-specific transport. The source diagram shows the path through middleware, validation, execution and translation.

![Uber’s MCP gateway routes calls through middleware, validation, execution and service-specific transports.](images/source-05.webp)

*Source: ByteByteGo’s article. Tap to enlarge; the complete figure is preserved.*
