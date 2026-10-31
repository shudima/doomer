---
schema_version: 2
id: uber-mcp-gateway-31398518-009
title: Follow a call through the gateway
background_image: images/network.svg
source_url: https://blog.bytebytego.com/p/how-uber-built-a-gateway-for-ai-agents
source_file: null
source_title: How Uber Built A Gateway For AI Agents To Access Tools
source_type: article
source_locator: 'Section: How Uber’s MCP Gateway Works; added illustrative example'
sort_order: 6
language: en
---

**Illustrative example**

An agent asks for an incident’s details. The gateway identifies the tool, validates its input, checks the caller and translates the request for the backing service.

It then returns a usable result. The agent does not need to know every service’s transport, but the shared entrance still has to enforce access on each call. This is an added walkthrough of the architecture.
