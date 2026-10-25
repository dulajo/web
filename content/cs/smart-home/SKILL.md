---
name: smart-home
description: Chytrá domácnost, která šetří čas a nepřidělává starosti. Máte ji, nebo ji teprve chcete? Podíváme se na to spolu. Použijte, když chcete dům, který funguje spolehlivě. Nepoužívejte na elektroinstalaci.
---

# Chytrá domácnost

Jsem programátor a náš dům řídíme přes Loxone doplněný o Home Assistant. Máme svého domácího asistenta, který má k domu všechny podklady, takže je nedohledáváme v papírech, tabulkách a e-mailech. Rád se podívám i na ten váš.

## Kdy se vám hodím

- Máte chytrou domácnost, ale zařízení spolu mluví asi jako sousedi přes plot
- Chytrou domácnost nemáte, ale chtěli byste ji a rádi byste probrali možnosti
- Stavíte nebo rekonstruujete: projdeme, co má smysl připravit už teď, aby se později nemuselo sekat do hotových zdí
- Nechcete automatizovat celý dům, ale rádi byste zautomatizovali aspoň agendu kolem něj: záruky, pojistky, servis
- Chcete doma vlastní server (homelab) a data mít u sebe, ne „někde v cloudu“
- Chcete domácího AI asistenta, který odpovídá z vašich podkladů, ne z hlavy

## Příklady

**Vstup:** V jedné místnosti chci uklízet, jinde večer odpočívat.
**Výstup:** Scéna Úklid pustí v místnosti plný jas a bílé světlo. Večerní režim pro celý dům zařídí, že všechna světla, která se rozsvítí, svítí jen na 40 % a teple žlutě.

**Vstup:** Odcházíme z domu a nechceme nic hlídat.
**Výstup:** Jedno tlačítko u dveří za 30 sekund zapne alarm a režim nepřítomnosti, který mimo jiné vypne cirkulaci teplé vody. Když zůstalo otevřené okno, přijde notifikace a hlavně zabliká světlo v zádveří, protože notifikace si člověk většinou všimne až pozdě. Při návratu čtečka otisků na dveřích alarm i režim nepřítomnosti zase vypne.

**Vstup:** V létě jsme v novostavbě bojovali s vysokou vlhkostí a k tomu byla vedra.
**Výstup:** Rekuperace má letní režim: když je doma vlhko a plný výkon pomůže vlhkost snížit, rozjede se naplno. Když by naopak přivedla vlhčí vzduch zvenku, naplno se nepustí ani v režimu boost.

**Vstup:** Hledání záručního listu nebo smlouvy znamenalo přehrabovat šuplíky a složky.
**Výstup:** Dokumenty jsou v domácím správci dokumentů a asistent je najde za pár vteřin.

**Asistent:** Dnes měla být kontrola tepelného čerpadla. Proběhla? Máme z ní zprávu? Pokud ano, pošli mi ji, stejně jako fakturu za práci. Mám si k tomu poznamenat ještě něco, co se ze zprávy nedočtu? Pokud neřekneš jinak, za 11 měsíců ti připomenu objednat další servis.

**Asistent:** Dnes mám v agendě objednat servis rekuperace. V e-mailu máš připravený koncept, zkontroluj ho a odešli.

Objednat by to zvládl i sám, ale poslední slovo zatím chceme mít my.

**Ty:** Udělej analýzu tepelka za poslední měsíc.
**Asistent:** Tepelné čerpadlo je v pořádku, za posledních 30 dní jsem nenašel žádnou poruchu a topí úsporně. Prostor pro úsporu vidím jinde: noční program topí na 22 °C, přes den jen na 21 °C, a cirkulace teplé vody pořád běží asi 1,5 hodiny denně. Úprava obojího a pokus topit spíš odpoledne by mohly ušetřit zhruba 1 000–2 000 Kč ročně. Nic jsem neměnil.

## Co k tomu potřebujete

- Nic speciálního. Loxone, Home Assistant ani vlastní server mít nemusíte.
- Kde asistent běží a kam posílá data, jsou dvě různé věci. Běžet může na vašem počítači nebo na samostatném domácím počítači. Pokud ale používá AI v cloudu, část dat jí posílá. Kdo nechce, aby cokoli opustilo dům, potřebuje vlastní AI model na silnějším domácím hardwaru. Vybereme podle toho, co potřebujete.
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

## Na co se nehodím

- Elektroinstalace. Jsem programátor a architekt řešení, ne elektrikář.

## Ozvěte se

Máte doma něco, co nefunguje, jak byste chtěli, nebo chytrou domácnost teprve promýšlíte? Napište mi, co řešíte. Probereme, jestli a jak bych mohl pomoct.

- E-mail: dulajosef@gmail.com
- LinkedIn: [linkedin.com/in/josef-dula-530505b3](https://www.linkedin.com/in/josef-dula-530505b3)
