---
schema_version: 2
id: common-questions-about-agent-evals-7b591106-018
title: Check the action and the answer
background_image: images/background.svg
source_url: https://www.langchain.com/blog/common-questions-about-agent-evals
source_file: null
source_title: The Most Common Questions About Agent Evals, Answered
source_type: article
source_locator: 'Section: What are the different types of agent evaluators?; added illustrative example'
sort_order: 8
language: en
---

**Illustrative example**

A travel assistant says it booked Friday’s flight under the budget. Check the booking record: the price is right, but the date is Saturday.

The message alone sounds successful. A date assertion on the action catches the real failure. Keep a separate check for whether the final answer accurately describes the booking.
