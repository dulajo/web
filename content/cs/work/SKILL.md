---
name: work
description: Seniorní backend vývojář z banky, který převezme celou věc od zadání po provoz. Použijte, když stavíte systém, který nesmí spadnout: nasazení bez výpadku, zpětná kompatibilita a záložní plán pro chvíli, kdy se něco pokazí. Tiket nepřepisuju rovnou do kódu, nejdřív zjistím, co tím autor myslel. Nepoužívejte, pokud hledáte někoho na celodenní schůzky.
location: Praha
---

# Josef Dula

10 let v oboru. Pomáhal jsem postavit banku od nuly. V malém týmu provozujeme a vyvíjíme kartový systém pro statisíce karet a všechny jejich transakce. Jako jediný backend vývojář jsem postavil první nákup bitcoinu přímo v bance v Česku. A teď jsem ve skupině, která v bance řídí AI.

Releasy dělám bez výpadku, protože vysvětlovat lidem, proč jim nejde karta, mě nebaví. Nejvíc mě naopak baví podívat se do dat a vidět, kolik lidí používá to, co jsem postavil.

## Kdy se vám hodím

- Stavíte systém, který nesmí spadnout ani ztratit data. Ani v pátek odpoledne.
- Potřebujete někoho, kdo vezme celý úkol: vyjasní zadání, rozplánuje ho po krocích, dostane ho do produkce a nezmizí hned po merge
- Chcete vydávat bez výpadků: zpětně kompatibilní změny a vždycky připravená cesta zpátky
- Chcete AI v produkci, ne v prezentaci

## Jak pracuju

- Tiket není zadání. Je to začátek rozhovoru, občas i výslechu.
- Celý úkol od začátku do konce: zadání, plán po etapách, cesta do produkce, observabilita a monitoring, abych věděl, že to opravdu funguje.
- Release bez výpadku je standard, ne svátek.
- Co může být deterministické, má být deterministické. Agent má zavolat nástroj, ne si pokaždé znovu tipnout.
- Hotovo je, až to lidé používají. Do té doby je to jen hezký kód.

## Schopnosti

- jazyky: Kotlin, Java, SQL, PL/SQL, TypeScript
- backend: Spring, Micronaut, Quarkus, Hibernate, Liquibase, Gradle, PostgreSQL, Oracle, DynamoDB
- provoz: nasazení bez výpadku, zpětná kompatibilita, idempotence, záložní scénáře, observabilita a monitoring
- platby: vydávání a zpracování karet, Visa (Click to Pay, Apple Pay), clearing, Stripe
- ai: LLM agenti, volání nástrojů, MCP, ACP, sandboxing agentů, znalostní báze
- infra: AWS, Terraform, Docker
- doručení: technické specifikace, plán po etapách, architektonická rozhodnutí, řízení týmové operativy

## Příklady

**Vstup:** Banka chtěla být první v Česku, kde si klienti koupí bitcoin přímo v bance.
**Výstup:** Celý backend jsem postavil jako jediný backend vývojář, s AI po boku. Idempotentní architektura, která zvládá produkční provoz i velké objemy. Jsme v produkci, transakce lítají a žádný vážný bug.

**Vstup:** Clearingové soubory karet začaly s rostoucím počtem transakcí drhnout.
**Výstup:** Přepracoval jsem zpracování clearingu. Teď v klidu stíhá statisíce karet a miliony plateb.

**Vstup:** Malí obchodníci v EU potřebovali jednoduše přijímat bezhotovostní platby.
**Výstup:** Aplikace Trisbee s kompletní integrací na Stripe: karty, Apple Pay, Google Pay i měsíční předplatné, včetně interního účetního systému.

## Historie verzí

### v3.2 — + AIVengers (říj 2026 – dosud)
- Přidáno: člen AIVengers, malé skupiny, která řídí AI napříč bankou

### v3.1 — + Tech Lead Platform (2025 – dosud)
- Přidáno: člen Tech Lead Platform, která určuje technický směr firmy. Stejná role, nové funkce, zpětně kompatibilní.

### v3.0 — Senior Backend Engineer, karty @ PBK Technology / Partners Banka (čvc 2023 – dosud)
- Začátek: nastoupil jsem ještě před spuštěním banky, nové banky na zelené louce a v moderních technologiích
- Přidáno: kartový tým od prvního dne; velmi malý tým, který provozuje statisíce karet a miliony plateb
- Přidáno: kompletní napojení na Visu včetně Click to Pay a Apple Pay
- Zlepšeno: zpracování clearingových souborů při rostoucím objemu transakcí
- Přidáno: nákup bitcoinu přímo v bance, první v Česku; jediný backend vývojář, idempotentní architektura pro produkční objemy

### v2.1 — CTO @ Trisbee (bře 2023 – čvn 2023)
- Změněno: pár měsíců jako CTO malého startupu: provoz, Jira, náklady na AWS, správa hesel, technický směr

### v2.0 — Backend vývojář @ Trisbee (čvc 2020 – úno 2023)
- Přidáno: platební metoda pro malé obchodníky v EU, postavená v malém mezinárodním týmu
- Přidáno: klíčové platební komponenty a interní účetní systém
- Přidáno: Stripe: karty, Apple Pay, Google Pay, měsíční předplatné
- Přidáno: integrace s Mailgunem, HubSpotem, AWS a Zapierem; analýzy a reporting

### v1.0 — Integrační vývojář @ Provys (2016 – 2020)
- Začátek: PL/SQL integrace mezi systémy (SQL, XML, SOAP, JSON)
- Přidáno: migrace velkých televizí: TV Nova, TVE, BT Sport
- Přidáno: týmová operativa: rozdělování práce a odhady kapacity
- Přidáno: spolutvorba interního dokumentačního systému

### v0.1 — Ing., Informační systémy a technologie @ VŠE Praha (2012 – 2018)

## Mimo práci

- **Chytrá domácnost a automatizace** — po práci s obojím pomáhám dalším lidem. Viz [smart-home](/cs/smart-home/) a [automation](/cs/automation/).
- **Volno** — hlavně beach volejbal.

## Na co se nehodím

- Celé dny na schůzkách a akademické debaty, ze kterých nic nevzejde.
- Práce, kde jde víc o vykazování než o výsledky. Potřebuju tvořit a vidět, že to funguje.
- Nechat LLM hádat, kolik je 2 + 2.

## Ozvěte se

Řešíte podobné věci, nebo stavíte něco zajímavého? Napište mi.

- E-mail: dulajosef@gmail.com
- LinkedIn: [linkedin.com/in/josef-dula-530505b3](https://www.linkedin.com/in/josef-dula-530505b3)
- GitHub: [github.com/dulajo](https://github.com/dulajo)
