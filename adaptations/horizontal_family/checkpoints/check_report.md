# Check report — famiglia orizzontale (Check 1–4)

Metodo: misure automatiche dei bounding box (`src/render_horizontal.mjs --measure`) sulle tre size ai momenti di hold (1,60 · 3,50 · 5,00 · 6,80 · 9,00 s) e a passo 20 ms nelle finestre di morph (7,72–7,82 s); sequenza campione di 50 fotogrammi (5 fps) per size per la fascia disclaimer; ispezione a 100 % di wireframe, styleframe e storyboard. Nessun controllo in FAIL alla consegna; dove un controllo è fallito nella prima iterazione sono riportati correzione e nuovo esito.

## Check 1 — Wireframe (griglia, proporzioni, margini, ordine di lettura, CTA, safe, equilibrio)

| Controllo | 1920×1080 | 300×250 | 336×280 | Esito | Problema | Correzione | Nuovo risultato |
|---|---|---|---|---|---|---|---|
| Griglia dichiarata (margine / colonne / gutter) | 96 / 12 / 32 | 16 / 6 / 8 | 18 / 6 / 8 | PASS | — | — | — |
| Asse: cx di titolo, regolo, hero, CTA, titolo S5 = W/2 ± 0,5 | 960,0 | 150,0 (titolo 150,0 · CTA 150 · card 150) | 168,0 | PASS | — | — | — |
| Riga di card S5 centrata (1920) / righe a filo margine (rettangoli) | 200–1720 → cx 960 | x 16, w 268 | x 18, w 300 | PASS | — | — | — |
| Ordine di lettura S1: BONUS → SPORT (sx→dx) → CTA (sotto) | ✔ | ✔ | ✔ | PASS | — | — | — |
| Ordine di lettura S5: titolo → Sisal → NetBet → William Hill → CTA | sx→dx | alto→basso | alto→basso | PASS | — | — | — |
| Centro ottico S1 (titolo+regolo+CTA) Δ ≤ 8 px | +3 | −1 | −1 | FAIL → PASS | prima iterazione: blocco S1 a 300–694 su 1920 (Δ +23), +6/+6 sui rettangoli | S1 alzato di 20 px (1920) e 4 px (rettangoli) | Δ +3 / −1 / −1 |
| Centro ottico S2–S4 (card+CTA) Δ ≤ 8 px | +3 | +1 | +2 | FAIL → PASS | prima iterazione Δ +31 (1920: card 170–670, CTA 730–840) | hero e CTA alzati di 28 px | 142–812 → Δ +3 |
| Padding/struttura identici tra le tre card/righe S5 | 52/202/252 | pad 12, colonna 62 | pad 14, colonna 68 | PASS | — | — | — |
| Spaziatura tra card/righe costante | 40 | 4 | 4 | PASS | — | — | — |
| CTA presente in ogni scena, mai nella fascia | fondo max 863 / 972 | 203,4 / 220 | 225,6 / 246 | PASS | — | — | — |
| CTA leggibile (corpo ≥ 12, una riga) | 44/40/40 | 13/13/12 | 14/14/13 | PASS | — | — | — |
| Safe area continua, dichiarata in px | 108 | 30 | 34 | PASS | — | — | — |
| Nessun elemento sotto y = usable (50 fotogrammi per size) | dev. 0 | dev. 0 | dev. 0 | PASS | — | — | — |
| Margini laterali del titolo S1 ≥ margine griglia | 318 / 318 | 27 / 27 | 31 / 31 | PASS | — | — | — |

## Check 2 — Styleframe (peso ottico, tipografia, loghi, contrasto, colori, coerenza con il 970×250)

| Controllo | 1920×1080 | 300×250 | 336×280 | Esito | Problema | Correzione | Nuovo risultato |
|---|---|---|---|---|---|---|---|
| Loghi non deformati: rapporto box `<img>` = rapporto file (3,136 · 3,839 · 3,000) | 3,136 · 3,839 · 3,000 | 3,13 · 3,83 · 3,00 | 3,13 · 3,85 · 3,00 | PASS | — | — | solo `width`, mai `height` |
| Pesi ottici loghi (1 : 0,95 : 1,17 come master) | 520/494/610 · 300/285/350 | 124/118/146 · 62/59/72 | 136/130/160 · 68/65/80 | PASS | — | — | — |
| Gerarchia (valore > logo > CTA > titolo S5 > FINO A) | ✔ | ✔ | ✔ | PASS | — | — | — |
| FINO A ≥ 10 px | 36 / 30 | 10 / 10 | 11 / 10 | PASS | — | — | limite dichiarato sui rettangoli |
| Importi su una riga, € stesso corpo; valore nella colonna (righe) | ✔ | 61,1 in 62 | 66,1 in 68 | PASS | — | — | testo allineato a destra: nessun taglio |
| Contrasto bianco/card ≥ 7:1 · CTA ≥ 4,5:1 | ≈ 12:1 · 9,6:1 | idem | idem | PASS | — | — | — |
| Palette = token del master | ✔ | ✔ | ✔ | PASS | — | — | — |
| Titolo: BONUS bianco / SPORT lime su una riga | ✔ | ✔ | ✔ | PASS | — | — | — |
| Sfondo: stesso still, cerchio di centrocampo riconoscibile | ✔ (16:9) | ✔ | ✔ | PASS | — | — | — |
| Raccordo sfondo → fascia | 44 px | 22 px | 22 px | FAIL → PASS | prima iterazione: dissolvenza di 22 px fissa, troppo corta a 1080p | altezza per size (44 px su 1920) | fascia piatta, dev. 0 |
| Nessun effetto vetro / anello | ✔ | ✔ | ✔ | PASS | — | — | — |
| Coerenza con il 970×250 (`master_vs_horizontal_family.png`) | ✔ | ✔ | ✔ | PASS | — | — | — |

## Check 3 — Storyboard (ingressi, hold, transizioni, sovrapposizioni, CTA, finale, safe)

| Controllo | Esito | Evidenza | Problema | Correzione | Nuovo risultato |
|---|---|---|---|---|---|
| Ordine di ingresso S1: BONUS 0,20 → SPORT 0,38 → regolo 0,90 → CTA 0,90–1,30 | PASS | K1/K2 | — | — | — |
| Hold S1 a fuoco ≥ 0,6 s | PASS | K2 | — | — | — |
| Wipe orizzontale (skew −14°) confinato all'area utile | PASS | K3 + scansione fascia | — | — | — |
| Hero: card → logo → FINO A → cifre; dati completi a +0,95 s; hold ≥ 0,55 s | PASS | K4–K6 | — | — | — |
| Nessuna sovrapposizione CTA/card nei morph (elementi con opacità > 5 %) | FAIL → PASS | passo 20 ms 7,72–7,82 | prima iterazione: righe S5 dei rettangoli in salita di 8 px, gap con la CTA 3,6 px (300×250) / 5,7 (336×280) a opacità 0,33 | salita delle righe ridotta a 4 px (1920 invariato: 48 px, gap 32) | gap minimo visibile 32 / 6,8 / 8,8 px |
| S5: titolo + tre card/righe insieme, hold ≥ 1,55 s | PASS | K7 | — | — | — |
| Finale: due pulse (8,90 / 9,55), ultimo fotogramma completo | PASS | K8 | — | — | — |
| Pulse entro i bordi | PASS | 1920: x 686–1234; 300: 66,6–233,4; 336: 74,1–261,9 | — | — | — |
| Safe area libera su 150 fotogrammi campione | PASS | deviazione 0 | — | — | — |
| Durata 10,0 s · 25 fps · con audio (profilo `vertical` + pan L→R) | PASS | motion_system.md | — | — | — |

## Check 4 — Verifica a dimensione reale (100 %)

| Controllo | 1920×1080 | 300×250 | 336×280 | Esito | Note |
|---|---|---|---|---|---|
| Frame nativi ispezionati (S1, hero, S5) | ✔ | ✔ | ✔ | PASS | `styleframes/`, `storyboard/` |
| "FINO A" leggibile | 36/30 | 10/10 | 11/10 | PASS | Inter 600 maiuscolo con tracking |
| Importi leggibili, nessuna collisione con i bordi | ✔ | colonna 62, testo 61,1 | colonna 68, testo 66,1 | PASS | filo destro a 12 / 14 px dal bordo card |
| Loghi nitidi | ✔ | William Hill 72 px in riga 38 | 80 px | PASS | script sottile leggibile a 100 % |
| CTA su una riga, accento visibile | ✔ | ✔ (12 px) | ✔ | PASS | |
| Nessun testo/decorazione entro 4 px dai bordi | ✔ | ✔ | ✔ | PASS | |
| Contact sheet | `comparative_storyboards/horizontal_family_contact_sheet.png` (+ overlay safe) | | | PASS | 1920 mostrato al 50 %, rettangoli al 100 % |
| Confronto con il master | `comparative_storyboards/master_vs_horizontal_family.png` | | | PASS | 8 momenti, mappatura 12 s → 10 s |

## Criticità residue dichiarate (nessuna in FAIL)
- **C1 · 300×250**: FINO A a 10 px e valore a 16 px nelle righe S5 sono il limite; gap CTA↔righe 6,8 px durante l'ingresso (a riposo 10 px). Alternativa: righe 36 px (valore 15 px) per un gap di 14 px — non applicata per non ridurre i corpi.
- **C2 · 1920×1080**: durata 10 s (famiglia) o 12 s (master): decisione al gate; il render 2× richiede il ritrasferimento del ritaglio 2389×1344 nativo (0 crediti) oppure render 1× diretto (vedi `family_system/background_strategy.md`).
- **C3 · rettangoli**: S5 a righe è una ricomposizione (non esiste nel master): logo a sinistra, dati a destra; struttura e corpi identici per i tre operatori.
- **C4 · font sostitutivi**: come il master.
