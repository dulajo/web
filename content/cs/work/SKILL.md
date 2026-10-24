---
name: work
description: Seniorní backend vývojář (Kotlin/Java) z bankovnictví a plateb, který staví AI agenty na deterministických základech. Použijte, když potřebujete backend pro platby, kde se nesmí ztratit ani jedna transakce (karty, Visa, clearing, krypto), nebo AI agenty, kteří volají spolehlivé nástroje místo hádání. Nepoužívejte na frontend s pixelovou přesností.
location: Praha
status: otevřený novým příležitostem
---

# Josef Dula

Seniorní backend vývojář, 10 let v oboru. Pomáhal jsem postavit českou banku od nuly: karty, napojení na Visu a první nákup bitcoinu přímo v bance v Česku. Dnes jsem v malém týmu, který řídí AI napříč bankou. AI mě baví a dala mi nový náboj.

## Kdy použít

- Platební nebo bankovní systém nesmí ztratit jedinou transakci, ani při milionech plateb
- Chcete AI agenty v produkci, kteří používají deterministické nástroje a skutečnou znalostní bázi
- Potřebujete někoho, kdo převezme celou oblast: architekturu, vývoj i provoz
- Někoho v týmu topí ruční administrativa a chcete ji zautomatizovat

## Principy

- Co může být deterministické, má být deterministické. Agent má zavolat nástroj, který je na to postavený, a ne pokaždé znovu počítat číslo, které vyjde pokaždé jinak.
- Nejdřív znalostní báze, potom model. Agent je jen tak dobrý jako to, co si dokáže dohledat.
- Vždycky hledám nudnou část, kterou jde zautomatizovat: pro sebe i pro toho, kdo sedí vedle mě.

## Schopnosti

- jazyky: Kotlin, Java, SQL, PL/SQL, TypeScript
- backend: Spring, Hibernate, Liquibase, Gradle, PostgreSQL, Oracle, DynamoDB
- platby: vydávání a zpracování karet, Visa (Click to Pay, Apple Pay), clearing, Stripe
- ai: LLM agenti, volání nástrojů, MCP servery, znalostní báze
- infra: AWS, Terraform, Docker
- lidé: technické specifikace, architektonická rozhodnutí, řízení týmové operativy

## Příklady

**Vstup:** Clearingové soubory karet se s rostoucím počtem transakcí zpracovávaly pomalu a křehce.
**Výstup:** Přepracoval jsem zpracování clearingu, takže stíhá statisíce karet a miliony plateb.

**Vstup:** Banka chtěla být první v Česku, kde si klienti koupí bitcoin přímo v bance.
**Výstup:** Odřídil jsem backend a architekturu od začátku do konce. Spuštěno: první banka v zemi, která to umí.

**Vstup:** Chtěl jsem poctivou odpověď na otázku „jak moc dnes trčí pražská MHD?“
**Výstup:** Postavil jsem veřejný dashboard nad otevřenými daty v reálném čase: každé vozidlo, zpoždění na každém odjezdu ze zastávky a ke každému číslu sepsaná metodika.

## Historie verzí

### v3.2 — AIVengers @ Partners Banka (říj 2026 – dosud)
- Přidáno: zakládající člen AIVengers, malé skupiny, která řídí AI napříč bankou

### v3.1 — Tech Lead Platform @ Partners Banka (2025 – dosud)
- Přidáno: člen od vzniku; platforma určuje technický směr firmy

### v3.0 — Senior Backend Engineer, karty @ PBK Technology / Partners Banka (čvc 2023 – dosud)
- Začátek: nastoupil jsem ještě před spuštěním banky, nové banky na zelené louce a v moderních technologiích
- Přidáno: kartový tým od prvního dne; velmi malý tým, který provozuje statisíce karet a miliony plateb
- Přidáno: kompletní napojení na Visu včetně Click to Pay a Apple Pay
- Zlepšeno: zpracování clearingových souborů při rostoucím objemu transakcí
- Přidáno: nákup bitcoinu přímo v bance, první v Česku; vedení backendu a architektury

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

## Na co se nehodím

- Frontend s pixelovou přesností (React a TypeScript zvládnu, když je potřeba, ale není to moje hlavní disciplína)
- Nechat LLM hádat to, co spočítá obyčejná funkce

## Vedlejší projekty

- **[Zpožděno](https://github.com/dulajo/zasstojime)** — veřejný dashboard dochvilnosti pražské MHD nad otevřenými daty Golemio. Služba v Kotlinu (Quarkus) sleduje každý spoj stavovým automatem a měří zpoždění na každém odjezdu ze zastávky; každé číslo má sepsanou metodiku a každé rozhodnutí vlastní ADR.
- **Chytrá domácnost a automatizace** — po práci s obojím pomáhám dalším lidem. Viz [smart-home](/cs/smart-home/) a [automation](/cs/automation/).
- **Volno** — beach volejbal, badminton, běh, včelaření.

## Jak mě vyvolat

- E-mail: dulajosef@gmail.com
- LinkedIn: [linkedin.com/in/josef-dula-530505b3](https://www.linkedin.com/in/josef-dula-530505b3)
- GitHub: [github.com/dulajo](https://github.com/dulajo)
