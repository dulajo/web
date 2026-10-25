---
name: smart-home
description: Chytrá domácnost, která šetří čas a nepřidělává starosti. Světla, žaluzie, topení i spotřebiče spolu konečně mluví a dům se o spoustu věcí postará sám, aniž byste o tom museli vědět. Máte chytrou domácnost? Podíváme se na ni, ať běží na čemkoli. Nemáte? Probereme, co by vám dávalo smysl. Použijte, když chcete dům, který funguje spolehlivě a předvídatelně. Nepoužívejte na elektroinstalaci.
---

# Chytrá domácnost

Jsem programátor a náš dům řídíme přes Loxone doplněný o Home Assistant. Máme svého domácího asistenta, který má k domu všechny podklady, takže je nedohledáváme v papírech, tabulkách a e-mailech. Rád se podívám i na ten váš.

## Kdy se vám hodím

- Máte chytrou domácnost, ale zařízení spolu mluví asi jako sousedi přes plot
- Chytrou domácnost nemáte, ale chtěli byste ji a rádi byste probrali možnosti
- Stavíte nebo rekonstruujete a chcete chytrou domácnost promyslet hned od začátku
- Nechcete automatizovat celý dům, ale rádi byste zautomatizovali aspoň agendu kolem něj: záruky, pojistky, servis
- Chcete doma vlastní server (homelab) a data mít u sebe, ne „někde v cloudu“
- Chcete domácího AI asistenta, který odpovídá z vašich podkladů, ne z hlavy

## Co k tomu potřebujete

- Nic konkrétního. Loxone, Home Assistant ani vlastní server mít nemusíte, nebo můžete mít všechno a ještě něco jiného. Níž popisuju jen to, jak to máme my.
- Domácího asistenta jde provozovat na několika úrovních. Nejjednodušší je aplikace na vašem počítači, která běží, jen když ji zapnete. O krok dál je samostatný, klidně starší počítač, který běží nonstop a vidí jen to, co mu dovolíte. A nejdál je propojení s chytrou domácností a čidly.
- Co asistent uvidí, máte pod kontrolou. Nechcete, aby vám lezl do e-mailu? Dostane vlastní schránku a přepošlete mu jen to, co má vidět. Nechcete mu dát celý Google Drive? Dostane vlastní účet a nasdílíte mu jen vybrané složky.

## Jak pracuju

- Nejdřív pochopím, co potřebujete, a pak navrhnu řešení, které vám sedí. Ne to, které je zrovna nejvíc cool.
- Automatizace mají šetřit čas a vy byste o nich skoro neměli vědět. Nemají přidávat starosti ani vás vytáčet.
- Když má AI jakkoli řídit dům nebo pomáhat s agendou, musí mít jasně daná pravidla a hranice, abyste se na ni mohli spolehnout.

## Co u nás doma běží

- Loxone jako základ: světla, žaluzie, rekuperace, tepelné čerpadlo a zabezpečení
- Home Assistant na zbytek: spotřebiče, kamery a složitější automatizace nad Loxonem
- Homelab s několika domácími službami, které nám šetří předplatné za velká řešení, třeba správce hesel nebo správce dokumentů
- Centrální mozek domu: podklady ke všemu na jednom místě, přehledně uspořádané
- Domácí asistent, který může pracovat s kteroukoli z těchto věcí, podle toho, co mu dovolíme
- Nejnovější přírůstek: 3D model celého domu. AI model Astra ho s pomocí bezplatného Blenderu překreslil z projektu domu, z aktuálních fotek do něj doplňuje nábytek a podle toho ladíme úpravy místností.

## Příklady

**Vstup:** Cirkulační čerpadlo teplé vody běželo pořád, i když teplou vodu nikdo nepotřeboval.
**Výstup:** Řídí ho kombinace přítomnosti, režimu domu a délky cyklu, která je opravdu potřeba. Běží jen tehdy, když to dává smysl.

**Ty:** Udělej analýzu tepelka za poslední měsíc.
**Asistent:** Tepelné čerpadlo běží krásně a všechny hodnoty jsou v normě. Jen koukám, že se jednou někdo sprchoval v době, kdy nebyla připravená teplá voda. Bojler nebyl vychladlý, ale pokud se plánujete sprchovat takhle brzy ráno, měli bychom upravit nastavení.

**Vstup:** Hledání záručního listu nebo smlouvy znamenalo přehrabovat šuplíky a složky.
**Výstup:** Dokumenty jsou v domácím správci dokumentů a asistent je najde za pár vteřin.

**Asistent:** Dnes měla být kontrola tepelného čerpadla. Proběhla? Máme z ní zprávu? Pokud ano, pošli mi ji, stejně jako fakturu za práci. Mám si k tomu poznamenat ještě něco, co se ze zprávy nedočtu? Pokud neřekneš jinak, za 11 měsíců ti připomenu objednat další servis.

**Asistent:** Dnes mám v agendě objednat servis rekuperace. V e-mailu máš připravený koncept, zkontroluj ho a odešli.

Objednat by to zvládl i sám, ale poslední slovo zatím chceme mít my.

## Na co se nehodím

- Elektroinstalace. Jsem programátor a architekt řešení, ne elektrikář.

## Ozvěte se

Máte doma něco, co nefunguje, jak byste chtěli, nebo chytrou domácnost teprve promýšlíte? Napište mi, co řešíte. Probereme, jestli a jak bych mohl pomoct.

- E-mail: dulajosef@gmail.com
- LinkedIn: [linkedin.com/in/josef-dula-530505b3](https://www.linkedin.com/in/josef-dula-530505b3)
