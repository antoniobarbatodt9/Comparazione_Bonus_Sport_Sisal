# Check report — famiglia verticale (Check 1–4)

Metodo: misure automatiche dei bounding box (`src/render_vertical.mjs --measure`) su tutte e tre le size ai momenti di hold (t 1,60 · 3,40 · 8,60 s) e su una sequenza campione di 50 fotogrammi (5 fps, 10 s) per la fascia disclaimer e le escursioni; controllo visivo a 100 % di wireframe, styleframe e storyboard. Nessun controllo in stato FAIL al momento della consegna: dove un controllo è fallito nella prima iterazione è riportata la correzione e il nuovo esito.

## Check 1 — Wireframe (griglia, proporzioni, margini, padding, ordine di lettura, CTA, safe, equilibrio)

| Controllo | 300×600 | 320×480 | 160×600 | Esito | Problema rilevato | Correzione | Nuovo risultato |
|---|---|---|---|---|---|---|---|
| Griglia dichiarata e rispettata (margini, colonne, gutter) | 24 / 6 / 12 | 20 / 6 / 12 | 12 / 4 / 8 | PASS | — | — | — |
| Asse centrale: cx di tutti gli elementi = W/2 ± 0,5 | 150,0 (tutti) | 160,0 (val 159,9–160,1) | 80,0 (tutti) | PASS | — | — | — |
| Margini laterali delle card = margine griglia | 24 | 20 | 12 | PASS | — | — | — |
| Margine superiore primo elemento S5 = m | titolo y 32 (m 24 + ascender) | 24 | 26 | PASS | — | — | — |
| Ordine di lettura S1: BONUS → SPORT → CTA (alto → basso) | ✔ | ✔ | ✔ | PASS | — | — | — |
| Ordine di lettura S5: titolo → Sisal → NetBet → William Hill → CTA | ✔ | ✔ | ✔ | PASS | — | — | — |
| Centro ottico S1 (blocco titolo+regolo+CTA) Δ ≤ 8 px | +8 | +6 | +4 | PASS | — | — | — |
| Centro ottico S2–S4 (card+CTA) Δ ≤ 8 px | +5 | +3 | −6 | PASS | — | — | — |
| Padding card identico tra le 3 card S5 | 12/52/66 | 8/44/56 | 10/52/66 | PASS | — | — | — |
| Spaziatura tra card costante | 12 | 10 | 8 | PASS | — | — | — |
| CTA presente in ogni scena, mai nella fascia | fondo max 494,2 / 540 | 405,9 / 430 | 497,4 / 544 | PASS | — | — | — |
| CTA leggibile a 100 % (corpo ≥ 12, una riga) | 18/17/17 | 17/16/16 | 12 | PASS | — | — | — |
| Safe area: fascia continua, dichiarata in px | 60 | 50 | 56 | PASS | — | — | — |
| Nessun elemento sotto y = usable (sequenza campione) | ✔ | ✔ | ✔ | PASS | — | — | — |
| Equilibrio: area vuota residua sotto la CTA in S1/S2 | 172 / 142 px | 130 / 102 px | 204 / 174 px | PASS | lo spazio sotto è "aria" coerente con il master (sfondo campo, cerchio) | — | — |

## Check 2 — Styleframe (peso ottico, tipografia, loghi, contrasto, colori, allineamenti, coerenza con il 970×250)

| Controllo | 300×600 | 320×480 | 160×600 | Esito | Problema | Correzione | Nuovo risultato |
|---|---|---|---|---|---|---|---|
| Rapporti loghi invariati (Sisal 3,10 · NetBet 5,51 · WH 4,83) | 3,13 · 3,85→ vedi nota | | | PASS | il rapporto misurato NetBet 95/24,7 = 3,85 in S5 è dovuto all'altezza misurata del box `<img>` con `height:auto` su PNG con padding trasparente; il file è lo stesso del master e non è deformato (width fisso, height auto) | — | PASS (nessuna deformazione: solo `width`, mai `height` forzata) |
| Peso ottico loghi calibrato (larghezze 1 : 0,947 : 1,167 come master) | 150/142/175 · 100/95/117 | 150/142/175 · 88/84/103 | 104/99/122 · 86/82/100 | PASS | — | — | — |
| Gerarchia tipografica (valore > logo > CTA > titolo S5 > FINO A) | ✔ | ✔ | ✔ | PASS | — | — | — |
| FINO A ≥ 10 px | 13 / 11 | 12 / 10 | 10,5 / **9,5** | FAIL → PASS | 160×600 card S5 FINO A a 9,5 px sotto il minimo | portato a 10 px (`fino.fs:10`) | 10 px, PASS |
| Importi su una riga, € stesso corpo | ✔ | ✔ | ✔ | PASS | — | — | — |
| Contrasto testo bianco / fondo card (≥ 7:1) | ≈ 12:1 | ≈ 12:1 | ≈ 12:1 | PASS | — | — | — |
| Contrasto CTA testo / lime (≥ 4,5:1) | ≈ 9,6:1 | idem | idem | PASS | — | — | — |
| Palette = token del master (verde, lime, ground, card 80 %, bordo 13 %) | ✔ | ✔ | ✔ | PASS | — | — | — |
| Titolo: BONUS bianco / SPORT lime, tracking finale −0,01 em | ✔ | ✔ | ✔ | PASS | — | — | — |
| Sfondo: stesso asset, stessa tinta, cerchio di centrocampo riconoscibile | ✔ | ✔ | ✔ | PASS | — | — | — |
| Nessun effetto vetro / anello (decisioni rev 2) | ✔ | ✔ | ✔ | PASS | — | — | — |
| Coerenza con il 970×250 (contact sheet master_vs_vertical_family.png) | ✔ | ✔ | ✔ | PASS | — | — | — |
| Raccordo sfondo→fascia disclaimer non brusco | — | — | — | FAIL → PASS | nel primo test la fascia piatta tagliava il campo con bordo netto | dissolvenza di 22 px dentro l'area utile (`#safe::before`), fascia intatta | PASS (fascia ancora piatta: deviazione 0) |

## Check 3 — Storyboard (ingresso, hold, transizioni, sovrapposizioni, CTA, finale, safe)

| Controllo | Esito | Evidenza | Problema | Correzione | Nuovo risultato |
|---|---|---|---|---|---|
| Ordine di ingresso S1: BONUS 0,20 → SPORT 0,38 → regolo 0,90 → CTA 0,90–1,30 | PASS | K1/K2 | — | — | — |
| Hold S1 con tutto a fuoco ≥ 0,6 s (1,30–2,00) | PASS | K2 | — | — | — |
| Wipe verticale confinato all'area utile; opacità 0 quando raggiunge y = usable | PASS | K3 + scansione fascia | — | — | — |
| Hero: card → logo → FINO A → cifre; dati completi a +0,95 s; hold ≥ 0,55 s | PASS | K4–K6 | — | — | — |
| Nessuna sovrapposizione CTA/card durante i morph e gli ingressi (solo elementi visibili, opacità > 5 %) | FAIL → PASS | misure a passo 20 ms in 1,80–2,50 · 7,00–8,00 · 8,80–10,00 | prima iterazione: a t 7,74 la terza card di S5 (opacità 0,33, in salita di 24 px) toccava la CTA ancora in morph (gap −1,5 px su 320×480, 4 px sulle altre) | morph 2 anticipato a 7,25–7,70 (CTA ferma prima dell'arrivo delle card) e salita delle card S5 ridotta a 12 px | gap minimo visibile: 14,4 (300×600) · 8,5 (320×480) · 10,8 (160×600) px, PASS |
| S5: titolo + tre card entrano insieme, hold ≥ 1,55 s | PASS | K7 | — | — | — |
| Finale: due pulse (8,90 / 9,55), nessun anello, ultimo fotogramma completo | PASS | K8 | — | — | — |
| Pulse 160×600 entro i bordi (x ≥ 4) | FAIL → PASS | prima iterazione 9 % → x 5,9; ridotto a 7 % + 5 % | ampiezza per size | x 7,3–152,7, PASS |
| Safe area libera su tutti i fotogrammi campione (150) | PASS | scansione pixel, deviazione 0 | — | — | — |
| Durata 10,0 s · 25 fps · 250 f · audio nessuno | PASS | motion_system.md | — | — | — |

## Check 4 — Verifica a dimensione reale (100 %)

| Controllo | 300×600 | 320×480 | 160×600 | Esito | Note |
|---|---|---|---|---|---|
| Frame a risoluzione nativa ispezionati (S1, hero, S5) | ✔ | ✔ | ✔ | PASS | `styleframes/`, `storyboard/` |
| "FINO A" leggibile a 100 % | 13/11 | 12/10 | 10,5/10 | PASS | Inter 600 maiuscolo con tracking: leggibile; 10 px è il limite dichiarato |
| Importi leggibili, nessuna collisione con i bordi card | margine int. ≥ 60 | ≥ 79 | ≥ 19 | PASS | |
| Loghi nitidi (PNG ufficiali ridotti con `width` intero) | ✔ | ✔ | ✔ | PASS | William Hill script sottile su 160: 100 px in S5, leggibile |
| CTA "SCOPRI DI PIÙ" su una riga, accento visibile | ✔ | ✔ | ✔ (12 px) | PASS | |
| Nessun testo/decorazione entro 4 px dai bordi | ✔ | ✔ | ✔ (pulse 7,3) | PASS | |
| Contact sheet a risoluzione nativa | `comparative_storyboards/vertical_family_contact_sheet.png` | | | PASS | + variante con overlay safe |
| Confronto con il master a risoluzione nativa | `comparative_storyboards/master_vs_vertical_family.png` | | | PASS | 8 momenti chiave, mappatura 12 s → 10 s |

## Criticità residue dichiarate (nessuna in FAIL)
- **C1 · 320×480**: margine CTA→safe a riposo 26 px (minimo famiglia). Alternativa se si vuole ≥ 30: card S5 a 80 px (valore 21 px). Non applicata per non ridurre i corpi.
- **C2 · 160×600**: FINO A a 10 px è il limite; l'alternativa (11 px) costa 4 px per card e porterebbe la CTA a 468. Mantenuto 10 con verifica a 100 %.
- **C3 · sfondo 2×**: per il render di produzione 2× serve il ritrasferimento del ritaglio 896×1344 (vedi background_strategy.md); a 1× i frame sono già definitivi.
- **C4 · font sostitutivi**: come il master (Montserrat/Inter dichiarati sostitutivi), nessun cambiamento in questa fase.
