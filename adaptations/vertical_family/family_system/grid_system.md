# Sistema di griglia della famiglia verticale

Fonte: master 970×250 concept M rev 2 (griglia implicita a 12 colonne, margine 26 px, gutter 20 px, safe area 40 px in basso — vedi `preflight_audit/layout_audit.md`). Le tre size condividono **una sola logica**: colonna centrale unica, asse verticale al centro, blocchi impilati dall'alto, fascia disclaimer in basso.

## Parametri per size (px)

| Parametro | 300×600 | 320×480 | 160×600 | Regola derivata dal master |
|---|---|---|---|---|
| Fascia disclaimer (safe) | 60 (y 540–600) | 50 (y 430–480) | 56 (y 544–600) | master 40/250 = 16 % → ≥ 10 % dell'altezza e ≥ 50 px |
| Area utile | 300×540 | 320×430 | 160×544 | tutto ciò che si anima vive qui |
| Margine superiore | 24 | 20 | 12 | master 26 (2,7 % larghezza) → 8 % larghezza |
| Margini laterali | 24 | 20 | 12 | idem |
| Colonne / gutter | 6 / 12 | 6 / 12 | 4 / 8 | 12 col del master dimezzate (300–320) o /3 (160) |
| Larghezza colonna | 30 | 35 | 25 | (W − 2m − (n−1)g)/n |
| Asse centrale | x = 150 | x = 160 | x = 80 | tutti i blocchi centrati sull'asse |
| Centro ottico | y ≈ 264 | y ≈ 209 | y ≈ 266 | metà area utile − 6 px (il peso del blocco sta un filo sopra la metà geometrica) |
| Padding card | 20 / 20 / 16 | 16 / 20 / 16 | 16 / 12 / 16 | master 22 / 22 / 18 (hero) |
| Spaziatura verticale titolo→CTA | rule + 26 | rule + 22 | rule + 18 | ≈ 1,2 × line-height del titolo |
| Spaziatura tra card | 12 | 10 | 8 | = gutter |
| Distanza card→CTA | 24 | 18 | 24 | ≥ margine |
| Area CTA S1 | 40,316 220×52 | 60,254 200×46 | 12,300 136×40 | vedi layout_spec |
| Area CTA operatore | 50,350 200×48 | 70,284 180×44 | 12,330 136×40 | |
| Area CTA confronto | 50,444 200×48 | 70,360 180×44 | 12,456 136×40 | |
| Distanza CTA → safe | 48 | 26 | 48 | ≥ 24 px (≥ 20 su 320×480, compensata con ombra corta) |
| Baseline titolo S1 | 176 / 226 (+lh 50) | 130 / 174 (+lh 44) | 200 / 234 (+lh 34) | blocco titolo+regolo+CTA centrato sul centro ottico |

## Regole comuni
1. **Un solo asse**: ogni elemento (titolo, regolo, card, logo, FINO A, valore, CTA) è centrato su x = W/2; tolleranza di verifica 0,5 px (misurata con `--measure`).
2. **Griglia verticale per blocchi**, non per righe fisse: i blocchi si impilano dall'alto con il margine come unità (m) e il gutter come sotto-unità (g).
3. **Centro ottico** per la scena S1 e per le hero card: il baricentro del blocco (titolo + regolo + CTA, oppure card + CTA) cade sul centro ottico ± 8 px.
4. **Scena S5** (confronto): titolo in alto al margine, tre card a passo costante, CTA sotto; la CTA non scende mai sotto usable − 24 px (usable − 26 su 320×480).
5. **Nessun elemento sotto y = usable**, particelle incluse (generate solo entro usable − 12).
6. Le misure di 320×480 sono **ricalcolate** (non copiate dal 300×600): margine 20, safe 50, colonna 35, card 84 px, titolo 40 px.

## Lista di verifica per size (eseguita in `checkpoints/check_report.md`)
- centro ottico e centro matematico del blocco principale in S1, S2–S4, S5;
- margini laterali reali delle card = m; margine superiore del primo elemento = m (S5);
- asse: cx di ogni elemento = W/2 (± 0,5);
- distanza CTA→safe ≥ 24 (≥ 26 su 320×480) su tutti i fotogrammi;
- fascia disclaimer piatta (`#061a12`) su tutti i fotogrammi campionati;
- leggibilità a 100 % del testo più piccolo (FINO A: 13 / 12 / 10 px).
