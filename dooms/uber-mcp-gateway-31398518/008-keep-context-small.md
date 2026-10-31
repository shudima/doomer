---
schema_version: 2
id: uber-mcp-gateway-31398518-007
title: Keep context small
background_image: images/network.svg
source_url: https://blog.bytebytego.com/p/how-uber-built-a-gateway-for-ai-agents
source_file: null
source_title: How Uber Built A Gateway For AI Agents To Access Tools
source_type: article
source_locator: 'Section: How the Uber MCP Gateway Deals With A Huge Catalog'
sort_order: 8
language: en
---

A large tool catalog does not have to fill the model’s context. **Omni MCP** discovers capabilities gradually, loading detail as the task needs it.

Response Projection returns selected fields instead of every part of a result. Code Mode lets coding agents work with results through files and shell commands. Together, these approaches keep the working context focused while leaving deeper information within reach.

![Omni MCP progressively discovers tools; Code Mode works with tool results through a command-line interface.](images/source-06.webp)

*Source: ByteByteGo’s article; credited to Uber Engineering in the article. Tap to enlarge; the complete figure is preserved.*
