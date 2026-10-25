---
name: work
description: Seniorní backend vývojář z banky, který převezme celou věc od zadání po provoz. Použijte, když stavíte systém, který nesmí spadnout. Tiket nepřepisuju rovnou do kódu, nejdřív zjistím, co tím autor myslel.
location: Praha
---

# Josef Dula

10 let v oboru. Pomáhal jsem postavit banku od nuly. V malém týmu provozujeme a vyvíjíme kartový systém pro statisíce karet a všechny jejich transakce. V šestičlenném týmu, kde jsem byl jediný backendista, jsme dodali první nákup bitcoinu přímo v bance v Česku. A teď jsem ve skupině, která v bance řídí AI.

Releasy dělám bez výpadku, protože vysvětlovat lidem, proč jim nejde karta, mě nebaví. Nejvíc mě naopak baví podívat se do dat a vidět, kolik lidí používá to, co jsem postavil.

## Kdy se vám hodím

- Stavíte systém, který nesmí spadnout ani ztratit data. Ani v pátek odpoledne.
- Potřebujete někoho, kdo vezme celý úkol: vyjasní zadání, rozplánuje ho po krocích, dostane ho do produkce a nezmizí hned po merge
- Chcete AI v produkci, ne v prezentaci
- Hledáte někoho, kdo táhne tým s sebou: pomůže kolegům a domluví řešení napříč týmy

## Příklady

**Vstup:** Banka chtěla být první v Česku, kde si klienti koupí bitcoin přímo v bance.
**Výstup:** V šestičlenném týmu jsem byl jediný backendista. Kryptoměny v bance předtím nikdo z nás nezaváděl a k tomu jsme silně regulované prostředí. Největší riziko bylo zpracovat platbu dvakrát nebo ji cestou ztratit, proto outbox pattern a důsledná idempotence: když okolní služba vypadne, zpracování se bezpečně zopakuje, bez zdvojené i ztracené platby. Za první čtvrtrok provozu jsme v produkci neopravovali jedinou chybu v našem kódu.

**Vstup:** Výkaz práce znamenal každý den vzpomínat, co jsem vlastně dělal, a ručně to naklikat.
**Výstup:** Dnes agent sám z podkladů navrhne, co jsem ten den dělal, a po mém schválení to vykáže. Jedna věta a jedno potvrzení. Spolu s automatizací release procesu je to jedna z věcí, které v AIVengers měníme od jejich vzniku.

**Vstup:** Agenti pro vývoj potřebují volné ruce, ale nesmí dostat celý vývojářův stroj ani firemní klíče.
**Výstup:** Navrhl jsem vývojářský sandbox: agent v něm pracuje bez neustálého schvalování, na síť smí jen na předem povolené adresy a API klíče ani tokeny se do sandboxu vůbec nedostanou, dosazuje je až proxy na cestě ven. Řešení teď přebírají další týmy v bance.

**Vstup:** Malí obchodníci v EU potřebovali jednoduše přijímat bezhotovostní platby.
**Výstup:** Aplikace Trisbee s kompletní integrací na Stripe: karty, Apple Pay, Google Pay i měsíční předplatné, včetně interního účetního systému.

## Jak pracuju

- Tiket není zadání, je to začátek rozhovoru.
- Velkou věc rozdělím na menší kroky, které jdou bezpečně nasadit, a mám nad nimi monitoring a data, abych věděl, že to v produkci opravdu funguje.
- Co může být deterministické, má být deterministické. Agent má zavolat nástroj, ne si pokaždé znovu tipnout.
- Hotovo je, až to lidé používají. Do té doby je to jen hezký kód.
- Nejlepší řešení vzniká v týmu. Rád pomáhám lidem kolem sebe, teď třeba učím kolegu z frontendu backend.

## Schopnosti

- jazyky: Kotlin, Java, SQL, PL/SQL, TypeScript
- backend: Spring, Micronaut, Quarkus, Hibernate, Liquibase, Gradle, PostgreSQL, Oracle, DynamoDB
- provoz: nasazení bez výpadku, zpětná kompatibilita, idempotence, záložní scénáře, observabilita a monitoring
- platby: vydávání a zpracování karet, Visa (Click to Pay, Apple Pay), clearing, Stripe
- ai: LLM agenti, volání nástrojů, MCP, ACP, sandboxing agentů, znalostní báze
- infra: AWS, Terraform, Docker
- doručení: technické specifikace, plán po etapách, architektonická rozhodnutí, řízení týmové operativy

## Historie verzí

### v3.2 — + AIVengers (říj 2026 – dosud)
- Přidáno: člen AIVengers, malé skupiny, která řídí AI napříč bankou

### v3.1 — + Tech Lead Platform (2024 – dosud)
- Přidáno: člen Tech Lead Platform, která určuje technický směr firmy: řešení napříč bankou, která pak přebírají ostatní týmy. Stejná role, nové funkce, zpětně kompatibilní.

### v3.0 — Senior Backend Engineer, karty @ PBK Technology / Partners Banka (srp 2023 – dosud)
- Začátek: nastoupil jsem ještě před spuštěním banky, nové banky na zelené louce a v moderních technologiích
- Přidáno: kartový tým od prvního dne; velmi malý tým, který provozuje statisíce karet a miliony plateb
- Přidáno: kompletní napojení na Visu včetně Click to Pay a Apple Pay
- Zlepšeno: zpracování clearingových souborů při rostoucím objemu transakcí
- Přidáno: nákup bitcoinu přímo v bance, první v Česku; jediný backendista v šestičlenném týmu, outbox pattern a idempotence

### v2.1 — CTO @ Trisbee (bře 2023 – srp 2023)
- Změněno: pár měsíců jako CTO malého startupu: vedení zhruba pětičlenného týmu, provoz, Jira, náklady na AWS, správa hesel, technický směr

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

- Práce, kde jde víc o schůzky a vykazování než o výsledky. Potřebuju tvořit a vidět, že to funguje.

## Ozvěte se

Řešíte podobné věci, nebo stavíte něco zajímavého? Napište mi.

- E-mail: dulajosef@gmail.com
- LinkedIn: [linkedin.com/in/josef-dula-530505b3](https://www.linkedin.com/in/josef-dula-530505b3)
- GitHub: [github.com/dulajo](https://github.com/dulajo)
