# 300×600 — specifica di layout (wide vertical)

Griglia: safe 60 (y 540–600) · area utile 300×540 · margini 24 · 6 colonne da 30 px, gutter 12 · asse x = 150 · centro ottico y ≈ 264. Wireframe: `wireframes/`, styleframe: `styleframes/`, storyboard: `storyboard/` (8 momenti chiave, con e senza overlay safe).

## S1 — titolo (0,00–2,00 s)
| Elemento | Box (x, y, w, h) | Tipo | Verifica |
|---|---|---|---|
| "BONUS" | 0,176 300×50 (testo centrato, 46/50) | Montserrat 800 46 px, bianco | cx 150,0 |
| "SPORT" | 0,226 300×50 | 46 px, lime | cx 150,0 |
| Regolo | 90,288 120×2 | lime 0,9 | cx 150 |
| CTA grande | 40,316 220×52, corpo 18 | lime, testo #06301d | cx 150; blocco 176–368 → centro 272 (ottico 264, Δ +8 ✔) |

## S2–S4 — hero card (2,30–7,40 s)
| Elemento | Box | Note |
|---|---|---|
| Hero card | 24,140 252×176, raggio 14 | padding 20 / 20 / 16; fondo card 80 %, bordo 13 % |
| Logo | box 24,160 252×64; larghezze Sisal 150 · NetBet 142 · William Hill 175 (altezze risultanti 48,3 · 25,8 · 36,2) | stessi rapporti del master (1 : 0,947 : 1,167) |
| FINO A | 24,236 252×16 · Inter 600 13 px | |
| Valore | 24,254 252×40 · Montserrat 800 34 px | "5.200€" = 132 px |
| CTA media | 50,350 200×48, corpo 17 | card + CTA: 140–398 → centro 269 (Δ +5 ✔) |

## S5 — confronto (7,70–10,00 s)
| Elemento | Box | Note |
|---|---|---|
| Titolo "BONUS SPORT" (una riga) | 0,32 300×30 · 26 px | bianco / lime |
| Regolo | 128,70 44×2 | |
| Card Sisal / NetBet / William Hill | 24,84 · 24,200 · 24,316 — 252×104, raggio 12, passo 116 (gap 12) | struttura identica: logo top 12 h 32 (larghezze 100 · 95 · 117), FINO A top 52 (11 px), valore top 66 (24/30) |
| CTA | 50,444 200×48, corpo 17 | fondo CTA 492 → 48 px sopra la safe; con pulse max (+9 %) fondo 494,2 |

## Decorazione
Particelle 14 (y < 528); flare in alto a sinistra (−60,−120 420×300); ombra centrale 24,90 252×380; wipe verticale limitato all'area utile. Nessun elemento oltre y = 540.
