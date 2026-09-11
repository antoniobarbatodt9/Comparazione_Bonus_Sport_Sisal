# 1920×1080 — specifica di layout (16:9)

Griglia: safe 108 (y 972–1080) · area utile 1920×972 · margini 96 · 12 colonne da 118, gutter 32 · asse x = 960 · centro ottico y ≈ 474. Wireframe: `wireframes/`, styleframe: `styleframes/`, storyboard: `storyboard/` (8 momenti, con e senza overlay safe; frame nativi 1920×1080).

## S1 — titolo (0,00–2,00 s)
| Elemento | Box (x, y, w, h) | Tipo | Verifica |
|---|---|---|---|
| "BONUS SPORT" (una riga) | 318,280 1283×190 (BONUS 318–957 bianco · SPORT 1006–1602 lime) | Montserrat 800 168 px | cx 960,0 |
| Regolo | 700,506 520×4 | lime 0,9 | cx 960 |
| CTA grande | 680,554 560×120, corpo 44 | lime, testo #06301d | blocco 280–674 → centro 477 (ottico 474, Δ +3 ✔) |

## S2–S4 — hero card (2,30–7,40 s)
| Elemento | Box | Note |
|---|---|---|
| Hero card | 510,142 900×500, raggio 40 | fondo card 80 %, bordo 13 % |
| Logo | box 510,198 900×180; larghezze Sisal 520 · NetBet 494 · William Hill 610 (altezze 165,8 · 128,7 · 203,3) | rapporti box = rapporti file (3,136 · 3,839 · 3,000): nessuna deformazione |
| FINO A | 510,413 900×39 · Inter 600 36 px | |
| Valore | 510,465 900×130 · Montserrat 800 112 px | "5.200€" = 429 px |
| CTA media | 700,702 520×110, corpo 40 | card + CTA: 142–812 → centro 477 (Δ +3 ✔); fondo 812 → 160 px sopra la safe |

## S5 — confronto (7,70–10,00 s)
| Elemento | Box | Note |
|---|---|---|
| Titolo "BONUS SPORT" | 624,92 672×100 · 88 px | cx 960 |
| Regolo | 900,214 120×4 | |
| Card Sisal / NetBet / William Hill | 200,278 · 720,278 · 1240,278 — 480×400, raggio 32, gap 40 | logo top 52 h 120 (larghezze 300 · 285 · 350), FINO A top 202 (30 px), valore top 252 (84/100) |
| CTA | 700,748 520×110, corpo 40 | fondo 858 → 114 px sopra la safe; con pulse 9 % fondo 863 |

## Decorazione
Particelle 40 da 5 px (y < 960); flare −300,−500 1600×1100; ombra centrale 180,120 1560×640; wipe 280 px skew −14° confinato all'area utile. Nessun elemento oltre y = 972.
