# Storyboard — Direzione A "Campo di luce" · 970×250 · 25 fps · 9,0 s · 225 fotogrammi · senza audio

> **Aggiornamento v2 (produzione, 2026-09-10)** — approvato con modifiche: etichetta di criterio rimossa, alone lime confermato, ordine confermato, durata 9,0 s confermata, richiesta di motion graphics di livello superiore. La timeline v2 e i fotogrammi definitivi sono in `frames_v2/` (safe area evidenziata) e `frames_v2_clean/`; il contact sheet aggiornato è `storyboard_v2_contact_sheet.png`. La sezione originale sotto resta come riferimento della prima consegna.

## Timeline v2 (motion design di produzione)

| t (s) | Evento | Dettaglio |
|---|---|---|
| 0,00 | CTA presente | Pill lime, visibile e integra per tutti i 225 fotogrammi |
| 0,00–0,70 | Ambiente | Dissolvenza dell'ambiente (still Higgsfield, 4 layer con parallasse: immagine, foschia, raggi, flare) |
| 0,10–1,60 | Riflettori | Il flare a destra "si accende" (0,10–0,55) e si assesta (0,55–1,60); i raggi entrano 0,30–1,40 |
| 0,25–1,08 | Titolo | "BONUS" e "SPORT" si rivelano da maschera, tracking da 0,14 em a −0,01 em; regolo lime 0,95–1,35 |
| 0,40–1,60 | Particelle | 22 punti luce deterministici compaiono e derivano lentamente (fermi nella GIF) |
| 0,90–1,70 | Card | Le tre card entrano **insieme**: salita 28 px, rotateX 16°→0, blur 5→0 px |
| 1,30–1,85 | Loghi | Dissolvenza + scala 0,94→1, simultanea |
| 2,00–2,35 | "FINO A" | Dissolvenza simultanea |
| 2,15–2,75 | Valori | Cifre una alla volta con maschera; **tutti i valori completi nello stesso istante (2,75 s)** |
| 3,05–3,75 | Riflesso vetro | Un riflesso diagonale attraversa le tre card **contemporaneamente** |
| 4,00–4,85 | Accento unico | Doppia luce (testa bianca + coda lime) percorre il bordo della card Sisal (un solo giro) |
| 4,55–6,10 | Accento si posa | Bordo lime 1,5 px (4,60–5,10) e alone (4,55–5,30), poi un unico assestamento (5,30–6,10) |
| 6,60–7,20 | CTA | Un solo riflesso diagonale |
| 6,10–9,00 | Fermo | Solo l'ambiente deriva (12 px, scala 1,04→1,00 sull'intera durata); end frame stabile |


**Immagini:** `frames/` (con safe area evidenziata in magenta, per lettura dello storyboard) e `frames_clean/` (senza overlay, come apparirà). Contact sheet: `storyboard_contact_sheet.png`. Ogni immagine è un fotogramma reale a 970×250 renderizzato dal progetto modificabile `08_progetto/banner.html` (ambiente: preview esplorativa Higgsfield #1, a bassa risoluzione; in produzione sarà rigenerato a risoluzione piena).

**Convenzione fotogrammi:** f = t × 25; f0 = primo fotogramma, f224 = ultimo (t = 8,96 s). Il file dura esattamente 9,00 s.

## Layout (px, origine in alto a sinistra)

| Zona | x, y | w × h | Note |
|---|---|---|---|
| Titolo "BONUS" / "SPORT" + criterio | 26, 48 | 190 × 100 | Montserrat 800, 37 px; "SPORT" in lime; criterio Inter 600, 10,5 px |
| Card Sisal | 232, 32 | 168 × 146 | raggio 12 px |
| Card NetBet | 420, 32 | 168 × 146 | identica |
| Card William Hill | 608, 32 | 168 × 146 | identica |
| Box logo (dentro ogni card) | +0, +22 | 168 × 40 | logo centrato; larghezze: Sisal 118, NetBet 112, William Hill 138 (equalizzazione per peso ottico, proporzioni intatte) |
| "FINO A" | +0, +76 | 168 × 13 | Inter 600, 11 px, tracking 0,14 em |
| Valore | +0, +94 | 168 × 38 | Montserrat 800, 29 px, cifre tabulari; **identico per i tre** |
| CTA "SCOPRI DI PIÙ" | 800, 83 | 150 × 44 | pill, lime, testo verde scuro, Montserrat 800 13,5 px |
| **Safe area disclaimer** | **0, 210** | **970 × 40** | **piatta `#061a12`, nessun elemento, nessun movimento, per tutta la durata** |
| Margine libero laterale | ≥ 20 px | — | nessun elemento tocca i bordi |

## Sequenza scena per scena

| Scena | t (s) | Fotogrammi | Immagine | Che cosa accade | Statico | Animato |
|---|---|---|---|---|---|---|
| 1 · Apertura | 0,00 | f0 | `scena_01_t0.00s` | Fondo verde-nero. **La CTA è già presente e leggibile** (ancora della composizione). Safe area vuota. | CTA, safe area | ambiente inizia la dissolvenza |
| 2 · L'ambiente si accende | 0,40 | f10 | `scena_02_t0.40s` | Il campo notturno emerge (dissolvenza 0–0,6 s). "BONUS" sta salendo (0,2–0,7 s), "SPORT" segue (0,3–0,8 s). | CTA, safe | ambiente, titolo |
| 3 · Titolo completo, arrivano le card | 1,00 | f25 | `scena_03_t1.00s` | Titolo fermo; "Importo massimo dichiarato" in dissolvenza (0,7–1,1 s). Le **tre card entrano insieme** (0,9–1,6 s, salita 22 px, stesso easing): tre superfici vuote e identiche. | titolo, CTA, safe | card, criterio |
| 4 · Identità | 1,50 | f38 | `scena_04_t1.50s` | Card quasi in posizione; i **tre loghi** appaiono in dissolvenza simultanea (1,25–1,75 s). Nessuna gerarchia: stessa opacità, stesso tempo. | titolo, CTA, safe | card (fine corsa), loghi |
| 5 · Il criterio | 2,20 | f55 | `scena_05_t2.20s` | Card e loghi fermi. "FINO A" appare sulle tre card (2,0–2,35 s); i valori iniziano a salire dietro la maschera (2,15–2,75 s). | titolo, card, loghi, CTA, safe | "fino a", valori |
| 6 · Rivelazione sincronizzata | 2,70 | f68 | `scena_06_t2.70s` | **5.200€ · 1.000€ · 255€** si stabilizzano nello stesso istante, stessa dimensione, stessa baseline. Da qui tutta l'informazione è leggibile. | tutto tranne l'ambiente | valori (ultimi px) |
| 7 · Fermo di lettura | 3,60 | f90 | `scena_07_t3.60s` | Nessun evento. Il lettore confronta i tre valori. L'ambiente deriva impercettibilmente. | tutto | ambiente (deriva) |
| 8 · L'accento | 4,40 | f110 | `scena_08_t4.40s` | **Unico accento**: un passaggio di luce lime percorre il bordo della card Sisal (4,0–4,85 s, 850 ms, un solo giro). Dimensioni e contrasto delle altre card invariati. | tutto | luce sul bordo Sisal |
| 9 · L'accento si posa | 5,00 | f125 | `scena_09_t5.00s` | Il passaggio finisce lasciando un **bordo lime 1,5 px** (4,6–5,1 s) e un alone tenue dietro la card (4,5–5,3 s). Fine di ogni animazione informativa. | tutto | bordo/alone (ultimi ms) |
| 10 · Riflesso CTA | 6,90 | f173 | `scena_10_t6.90s` | Un solo riflesso diagonale attraversa la CTA (6,6–7,2 s): richiama l'azione senza pulsare. | tutto | riflesso CTA |
| 11 · End frame | 9,00 | f224 | `scena_11_t9.00s` | Stato finale completo e stabile: titolo, criterio, tre card con logo e valore, bordo lime su Sisal, CTA, safe area libera. **Usabile come fallback statico.** | tutto | — |

## Gerarchia di lettura (verificata sui fotogrammi)
1. "BONUS SPORT" (dimensione + lime) → 2. i tre valori (bianco, 29 px, allineati) → 3. i tre loghi (stessa riga, stesso box) → 4. CTA (colore) → 5. criterio (piccolo, tono ridotto). Il bordo lime su Sisal non cambia questa gerarchia: agisce solo a livello 3 (identità) come accento, non a livello 2 (dati).

## Ruolo di Sisal nel banner
- Posizione di lettura primaria (prima card, ordine motivato dal criterio decrescente).
- Ambiente verde/lime coerente con il suo logo: identità "ambientale" condivisa da tutti gli operatori senza penalizzarli.
- Un solo accento (bordo di luce), stessa card, stesso valore, stesso logo-box degli altri.
- CTA nel lime del logo Sisal: il legame cromatico card Sisal ↔ azione è l'unico "privilegio" e non tocca i competitor.

## Uso dello spazio
970 px: 26–216 titolo · 232–776 tre card (544 px, gap 20) · 800–950 CTA. Verticale: 32–178 card, 210–250 safe area. Nessun elemento sotto y=210. Nessun elemento oltre x=950 o sotto x=20.

## Conclusione e loop
Riproduzione singola; end frame stabile per 3,9 s (5,1→9,0 s). In caso di loop forzato dal canale, la ripartenza (fondo scuro → dissolvenza ambiente) è morbida; nessuna transizione di loop aggiunta.

## Ruolo di Higgsfield MCP in questo storyboard
Solo l'**ambiente** (layer di fondo) è generato: still 21:9 "campo notturno generico", ritagliato e scurito. Tutto ciò che si legge — titolo, criterio, loghi ufficiali, "FINO A", importi, simbolo €, CTA — è composto separatamente dal progetto e resta modificabile. Dettagli e piano in `07_asset_generati/README_higgsfield.md`.

## Uso degli asset ufficiali
- `Sisal_white_neg_LRES.png` (2126×678) → 118 px di larghezza, altezza automatica (38 px), nessuna deformazione.
- `NetBet_PrimaryLogo_White.png` (837×218) → 112 px (20 px di altezza).
- `WilliamHill_white.png` (2172×724) → 138 px (29 px).
- Nel master finale i loghi verranno rasterizzati a 2× (deviceScaleFactor 2 in render, poi downsample) per massimizzare la nitidezza dei bordi a 1×; nessuna maschera o rettangolo dietro i loghi.
