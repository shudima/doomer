---
schema_version: 2
id: uber-mcp-gateway-31398518-006
title: Check the caller
background_image: images/network.svg
source_url: https://blog.bytebytego.com/p/how-uber-built-a-gateway-for-ai-agents
source_file: null
source_title: How Uber Built A Gateway For AI Agents To Access Tools
source_type: article
source_locator: 'Section: How the Gateway Takes Care of Access'
sort_order: 7
language: en
---

Access is checked for the caller, at server or individual-tool level. A result can also be redacted before it is returned.

For external integrations, Uber exchanges internal identity for the third-party credentials needed by that service. The agent does not gain unrestricted access merely because the tool appears in the catalog. Discovery, authorization and the contents of a response each need their own control.
