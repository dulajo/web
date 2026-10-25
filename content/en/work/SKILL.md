---
name: work
description: Senior backend engineer from a bank who owns a problem from requirements to production. Use when you are building a system that must not go down. I don't turn a ticket straight into code; first I find out what its author meant.
location: Prague, Czechia
---

# Josef Dula

10 years in. I helped build a bank from scratch. In a small team we run and develop the card system for hundreds of thousands of cards and all their transactions. In a team of six where I was the only backend engineer, we delivered the first in-bank bitcoin purchase in Czechia. And now I am in the group steering AI across the bank.

I ship without downtime, because explaining to people why their card doesn't work is not my idea of fun. What I do enjoy is looking at the data and seeing how many people use what I built.

## When I can help

- You are building a system that must not go down or lose data. Not even on a Friday afternoon.
- You need someone to take the whole task: clarify the requirements, plan it step by step, get it to production, and not vanish right after the merge
- You want AI in production, not in a slide deck
- You want someone who brings the team along: helps colleagues and agrees solutions across teams

## Examples

**Input:** The bank wanted to be the first in Czechia to let clients buy bitcoin directly in their bank.
**Output:** In a team of six I was the only backend engineer. None of us had brought crypto into a bank before, and we work in a heavily regulated environment. The biggest risk was processing a payment twice or losing it on the way, hence the outbox pattern and strict idempotency: when a surrounding service goes down, processing is safely retried, with no duplicated or lost payment. In the first quarter after launch, we didn't have to fix a single bug in our code in production.

**Input:** Filling in my timesheet meant trying to remember every day what I'd actually done, and clicking it in by hand.
**Output:** Now an agent drafts what I did that day from the available data, and once I approve, it's reported. One sentence and one confirmation. Together with automating the release process, it's one of the things we've been changing in AIVengers since day one.

**Input:** Coding agents need a free hand, but must not get the whole developer machine or the company's keys.
**Output:** I designed a developer sandbox: the agent works without constant approvals, can only reach pre-approved addresses, and API keys and tokens never enter the sandbox at all; a proxy adds them on the way out. Other teams across the bank are now adopting it.

**Input:** Small merchants in the EU needed a simple way to take cashless payments.
**Output:** The Trisbee app with a complete Stripe integration: cards, Apple Pay, Google Pay and monthly subscriptions, plus an internal accounting system.

## How I work

- A ticket is not a spec, it's the start of a conversation.
- I split a big thing into smaller steps that can be shipped safely, with monitoring and data on top, so I know it really works in production.
- If it can be deterministic, it should be. An agent should call a tool, not take another guess.
- Done means people use it. Until then it's just nice code.
- The best solutions come from the team. I like helping the people around me; right now I'm teaching a frontend colleague backend.

## Capabilities

- languages: Kotlin, Java, SQL, PL/SQL, TypeScript
- backend: Spring, Micronaut, Quarkus, Hibernate, Liquibase, Gradle, PostgreSQL, Oracle, DynamoDB
- operations: zero-downtime releases, backward compatibility, idempotency, backup scenarios, observability and monitoring
- payments: card issuing and processing, Visa (Click to Pay, Apple Pay), clearing, Stripe
- ai: LLM agents, tool calling, MCP, ACP, agent sandboxing, knowledge bases
- infra: AWS, Terraform, Docker
- delivery: technical specs, staged plans, architecture decisions, team operations

## Changelog

### v3.2 — + AIVengers (Oct 2026 – present)
- Added: member of AIVengers, a small group steering AI across the bank

### v3.1 — + Tech Lead Platform (2024 – present)
- Added: member of the Tech Lead Platform, which sets the company's technical direction: bank-wide solutions that other teams then adopt. Same role, new features, backward compatible.

### v3.0 — Senior Backend Engineer, Cards @ PBK Technology / Partners Banka (Aug 2023 – present)
- Initial: joined before the bank went live — a new bank built from scratch on a modern stack
- Added: cards team from day one; a very small team running hundreds of thousands of cards and millions of payments
- Added: full Visa integration, including Click to Pay and Apple Pay
- Improved: clearing file processing at growing transaction volume
- Added: in-bank bitcoin purchase, first in Czechia; the only backend engineer in a team of six, outbox pattern and idempotency

### v2.1 — CTO @ Trisbee (Mar 2023 – Aug 2023)
- Changed: a few months as CTO of a small startup — leading a team of about five, production, Jira, AWS costs, password management, technical direction

### v2.0 — Backend Developer @ Trisbee (Jul 2020 – Feb 2023)
- Added: payment method for small EU merchants, built in a small international team
- Added: core payment components and an internal accounting system
- Added: Stripe — cards, Apple Pay, Google Pay, monthly subscriptions
- Added: integrations with Mailgun, HubSpot, AWS and Zapier; analytics and reporting

### v1.0 — Integration Developer @ Provys (2016 – 2020)
- Initial: PL/SQL integrations between systems (SQL, XML, SOAP, JSON)
- Added: migrations of major broadcasters — TV Nova, TVE, BT Sport
- Added: team operations — splitting work and estimating capacity
- Added: co-built the internal documentation system

### v0.1 — Ing., Information Systems and Technology @ VŠE Prague (2012 – 2018)

## Outside work

- **Smart home and automations** — outside work I help people with both. See [smart-home](/smart-home/) and [automation](/automation/).
- **Off-duty** — mostly beach volleyball.

## Not a fit

- Jobs that are more about meetings and reporting than results. I need to build things and see them work.

## Get in touch

Solving similar problems, or building something interesting? Drop me a line.

- Email: dulajosef@gmail.com
- LinkedIn: [linkedin.com/in/josef-dula-530505b3](https://www.linkedin.com/in/josef-dula-530505b3)
- GitHub: [github.com/dulajo](https://github.com/dulajo)
