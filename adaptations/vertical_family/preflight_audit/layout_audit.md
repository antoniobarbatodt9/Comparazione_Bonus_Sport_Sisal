# Pre-flight audit · 2 — Layout, griglia, proporzioni, motion (ruoli: senior graphic / layout / motion / information / production designer)

## 2.1 Gerarchia visiva e ordine di lettura (master 970×250)
- S1: 1. "BONUS SPORT" (56 px, bianco+lime) → 2. CTA grande (lime). Lettura sinistra→destra su una riga.
- S2–S4: 1. logo (172–202 px) → 2. valore (38 px) → 3. "FINO A" → 4. CTA media. Lettura: card (sinistra) → CTA (destra).
- S5/S6: 1. i tre valori (29 px) → 2. i tre loghi → 3. CTA piccola (pulse) → 4. titolo (37 px, due righe). Lettura: titolo → card 1 → 2 → 3 → CTA.

## 2.2 Griglia utilizzata
- Griglia implicita a **12 colonne** su 970 px con margine laterale 26 px e gutter 20 px (colonna ≈ 56,5 px): titolo S5 = col 1–2 (26–222), card = col 3–5 / 6–8 / 9–11 (232–400 / 420–588 / 608–776), CTA = col 12 (800–950).
- Asse orizzontale: centro a y = 105 (area utile 0–210). S1 e S2–S4 sono composizioni **centrate come gruppo** (gruppo titolo+CTA 142–829 → centro 485,5 = centro formato; gruppo hero+CTA 195–775 → centro 485).
- Margini: laterali ≥ 20 px (min. effettivo 26 sinistra, 20 destra); superiore 30–32 px; inferiore (rispetto alla safe area a 210) 22–32 px.

## 2.3 Allineamenti, padding, spaziature
| Voce | Valore |
|---|---|
| Card S5: padding interno | logo-box top 22, altezza 40; "FINO A" top 76; valore top 94; bottom ≥ 14 |
| Card S5: gap | 20 px (identico) |
| Hero: padding | logo top 22 (h 56), "FINO A" 116, valore 134, bottom 16 |
| Distanza logo → "FINO A" | S5: 14 px · hero: 38 px |
| Distanza "FINO A" → valore | S5: 5 px · hero: 2 px (interlinea) |
| CTA: padding orizzontale | ≥ 18 px (testo centrato), altezza 44/52/54 → rapporto testo/altezza ≈ 0,31–0,38 |
| Titolo S1 ↔ CTA | 30 px |
| Titolo S5 ↔ card | 10 px |
| Card ↔ CTA (S5) | 24 px |

## 2.4 Rapporti e proporzioni ottiche
- Loghi: equalizzazione per **peso ottico** con rapporto costante 1 : 0,949 : 1,169 (Sisal : NetBet : William Hill) in ogni scena; proporzioni dei file intatte (verifica QC ±4 %).
- Valori: stesso corpo per i tre operatori in ogni scena; cifre tabulari; simbolo € inline, stesso corpo.
- CTA: sempre una pill (raggio 999), rapporto w/h ≈ 3,4–4,4; testo maiuscolo tracking 0,05 em.
- Card: rapporto 168/146 = 1,15 (S5), 300/158 = 1,90 (hero).

## 2.5 Tipografia e baseline
| Testo | Corpo / interlinea | Baseline (dal top del box) |
|---|---|---|
| Titolo S1 | 56 / 66 | ≈ 52 |
| Titolo S5 | 37 / 42 | ≈ 34 per riga |
| Valore hero | 38 / 46 | ≈ 36 |
| Valore card | 29 / 38 | ≈ 29 |
| "FINO A" hero / card | 13 / 16 · 11 / 13 | ≈ 12 · 10 |
| CTA grande / media / piccola | 20 · 18 · 13,5 | centrata otticamente (flex) |

## 2.6 Trattamento CTA e loghi
- CTA: unica, presente da 1,10 s alla fine; tre taglie collegate da morph continui; enfasi finale = solo pulse (+9 %, +6 %) ancorato al bordo destro; mai sopra la safe area.
- Loghi: PNG ufficiali bianchi, solo `width` impostata (height auto), nessuna maschera/patch, dissolvenza + scala 0,94→1 all'ingresso.

## 2.7 Zone di movimento e zone libere
- Movimento: titolo (S1), hero card (S2–S4), card (S5), CTA (morph/pulse), wipe (tutto il quadro sopra y=210), ambiente (deriva 14 px, camera per scena), particelle.
- Libere: safe area 0,210 970×40 (piatta, nessun elemento); margini laterali 0–20 / 950–970.

## 2.8 Struttura temporale
5 inquadrature + 4 transizioni identiche (0,30–0,35 s) + enfasi finale; clip operatore con coreografia e durata identiche (1,85 s).

## 2.9 Rapporto background/contenuto
Sfondo tinto e attenuato (ombra centrale 28 %, vignetta): le linee del campo restano ≤ 25 % di contrasto sotto testi e card; card all'80 % di opacità garantiscono contrasto ≥ 4,5:1 per i valori bianchi.

## 2.10 Punti di attenzione e problemi potenziali nel passaggio al verticale
| # | Rischio | Size più esposta | Mitigazione prevista |
|---|---|---|---|
| P1 | Sfondo 3,4:1 non copre un formato 1:2 / 1:3,75 | tutte | riframe **verticale dello stesso asset** (fascia centrale 896×1344 del job e190625a: cerchio di centrocampo + linea di metà campo verticale), nessuna nuova generazione |
| P2 | Titolo su una riga ("BONUS SPORT") non entra in 136–280 px | tutte | due righe impilate (come già in S5 del master), centrate |
| P3 | Card affiancate non entrano | tutte | card impilate verticalmente, stessa struttura interna (logo / FINO A / valore) |
| P4 | Logo William Hill (rapporto 4,83) in card di 136 px | 160×600 | larghezza max 100 px (padding 18), rapporto 1,169 mantenuto |
| P5 | "FINO A" sotto i 10 px | 160×600 | corpo minimo 9,5 px Inter 600 maiuscolo tracking 0,14 em; verificato a size reale |
| P6 | Wipe orizzontale troppo rapido su 160 px | 160×600 / 320×480 | wipe **verticale** (banda che scende), stessa durata 0,30 s |
| P7 | CTA grande di S1 e CTA nelle altre scene: percorso del morph in verticale | tutte | morph continuo lungo l'asse verticale, mai fuori quadro |
| P8 | Safe area: ombra/particelle/wipe non devono scendere nella fascia | tutte | particelle e wipe limitati a y < safe; fascia piatta `#061a12` sopra tutto |
| P9 | Durata 12 s → 8–10 s richiesti | tutte | timeline compressa proporzionalmente a 10,0 s (stessa sequenza narrativa) |
| P10 | Densità in 320×480 (5 blocchi in 430 px utili) | 320×480 | card 84 px con padding ridotti ma coerenti; corpi 22/10 px |
