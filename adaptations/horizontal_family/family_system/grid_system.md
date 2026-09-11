# Sistema di griglia della famiglia orizzontale

Fonte: master 970×250 (12 colonne, margine 26, gutter 20, safe 40) e famiglia verticale (asse unico, blocchi impilati, centro ottico). Le tre size condividono la logica: **asse verticale al centro, blocchi centrati, fascia disclaimer in basso**; 1920×1080 aggiunge la riga di tre card di S5 (come il master).

## Parametri per size (px)

| Parametro | 1920×1080 | 300×250 | 336×280 | Regola |
|---|---|---|---|---|
| Fascia disclaimer (safe) | 108 (y 972–1080) | 30 (y 220–250) | 34 (y 246–280) | ≥ 10 % dell'altezza (master 16 %) e ≥ 30 px |
| Area utile | 1920×972 | 300×220 | 336×246 | tutto ciò che si anima vive qui |
| Margini | 96 | 16 | 18 | 5 % della larghezza (master 2,7 %: qui i formati sono più bassi in proporzione) |
| Colonne / gutter | 12 / 32 | 6 / 8 | 6 / 8 | 12 col del master; 6 sui rettangoli |
| Larghezza colonna | 118 | 38 | 43 | (W − 2m − (n−1)g)/n |
| Asse | x 960 | x 150 | x 168 | ogni elemento centrato (± 0,5 px) |
| Centro ottico | y 474 | y 107 | y 120 | usable/2 − 1,2 % di usable |
| Hero card | 510,142 900×500 r40 | 16,22 268×118 r12 | 18,26 300×132 r12 | larghezza = 47 % / 89 % / 89 % |
| Card S5 | 3 × 480×400 (x 200 · 720 · 1240, y 278), gap 40 | 3 righe 268×38 (y 38 · 80 · 122), gap 4 | 3 righe 300×42 (y 42 · 88 · 134), gap 4 | 1920: gap = 1,25 gutter; rettangoli: gap = gutter/2 |
| Padding card S5 | logo top 52 · FINO A 202 · valore 252 | pad 12 (logo sx, dati dx) | pad 14 | identico tra le tre card |
| CTA S1 | 680,554 560×120 | 70,120 160×38 | 78,134 180×42 | |
| CTA hero | 700,702 520×110 | 70,158 160×36 | 78,178 180×40 | |
| CTA S5 | 700,748 520×110 | 70,170 160×32 | 78,188 180×36 | |
| Distanza card → CTA | 60 (hero) / 70 (S5) | 18 / 10 | 20 / 12 | ≥ gutter |
| Distanza CTA → safe (a riposo) | 114 (S5) / 160 (hero) | 18 (S5) / 26 (hero) | 22 (S5) / 28 (hero) | ≥ 16 px; con pulse 9 % il fondo scende di ≤ 5 px (1920) / ≤ 1,5 px |
| Regolo lime | 520×4 (S1) / 120×4 (S5) | 90×2 / 30×2 | 100×2 / 32×2 | |

## Regole comuni
1. **Asse unico**: cx = W/2 per titolo, regolo, hero, CTA, titolo S5 e per la riga di card (1920: gruppo 200–1720 centrato su 960).
2. **Blocchi centrati sul centro ottico** in S1 (titolo + regolo + CTA) e S2–S4 (card + CTA), tolleranza ± 8 px.
3. **S5**: titolo al margine superiore, card/righe a passo costante, CTA sotto; la CTA non scende mai sotto usable − 16.
4. **Nessun elemento sotto y = usable** (particelle generate solo entro usable − 12; wipe a opacità 0 fuori dall'area utile).
5. **Righe S5 (rettangoli)**: logo a sinistra a `pad`, colonna valore a destra di larghezza fissa (62 / 68) allineata a destra, "FINO A" a sinistra della colonna con gap 8: le cifre dei tre operatori sono a filo destro.
6. Le misure di 336×280 sono **ricalcolate** dal 300×250 (margine 18, safe 34, righe 42 px, titolo 36), non scalate.
