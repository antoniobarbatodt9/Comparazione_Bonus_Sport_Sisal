# Pre-flight audit · 2 — Layout, griglia, proporzioni, motion per i formati orizzontali

## 2.1 Tre formati, due famiglie di proporzione
| Size | Rapporto | Area utile (senza safe) | Natura | Parentela con il master |
|---|---|---|---|---|
| 1920×1080 | 16:9 (1,78) | 1920×972 | schermo intero (video, DOOH, social landscape) | come il master ma con **molta altezza**: il 970×250 (3,88:1) è una striscia; qui i blocchi possono respirare in verticale, la scena S5 torna a **tre card affiancate** come nel master |
| 300×250 | 1,2:1 | 300×220 | medium rectangle IAB | né striscia né verticale: titolo su una riga (come master), card impilate (come verticali) |
| 336×280 | 1,2:1 | 336×246 | large rectangle IAB | stessa logica del 300×250 ricalcolata (non scalata) |

## 2.2 Gerarchia e ordine di lettura (invariati)
- S1: "BONUS SPORT" su **una riga** (come nel master, non impilato: c'è larghezza) → regolo → CTA sotto, centrata.
- S2–S4: hero card centrata (logo → FINO A → valore) → CTA sotto la card (nel master è a destra: nei formati 1,2:1 e nel 16:9 la CTA sotto tiene il blocco compatto e centrato).
- S5: titolo in alto → Sisal → NetBet → William Hill → CTA. Su 1920×1080 le card sono **affiancate** (lettura sinistra → destra come nel master); su 300×250 e 336×280 sono **tre righe** (logo a sinistra, FINO A + valore a destra) perché tre card affiancate in 268 px darebbero loghi da 60 px illeggibili.

## 2.3 Griglie
| Size | Margine | Colonne / gutter | Colonna | Asse | Centro ottico (area utile) |
|---|---|---|---|---|---|
| 1920×1080 | 96 | 12 / 32 | 118 | x 960 | y 474 (972/2 − 12) |
| 300×250 | 16 | 6 / 8 | 38 | x 150 | y 107 |
| 336×280 | 18 | 6 / 8 | 43 | x 168 | y 120 |

## 2.4 Punti di attenzione (P) e mitigazioni previste
| # | Rischio | Size | Mitigazione |
|---|---|---|---|
| P1 | Sfondo 21:9 del master (2036×596) non copre 1920×1080 | 1920×1080 | ri-inquadratura **16:9 dello stesso still** (2389×1344 → 1920×1080), 0 crediti, nessun upscale |
| P2 | Titolo a 168 px su 1920: peso eccessivo o troppo "TV" | 1920×1080 | 168/190 = 8,75 % dell'altezza del quadro (master 56/250 = 22 %): meno invadente del master in proporzione, verificato a 100 % |
| P3 | Hero card su 16:9: card troppo grande = "cartello", troppo piccola = vuoto | 1920×1080 | card 900×500 (47 % × 51 % dell'area utile), logo 520 px, valore 112 px; la CTA sotto chiude il blocco (centro ottico Δ ≤ 8 px) |
| P4 | Tre card affiancate in 268/300 px | 300×250, 336×280 | S5 a **righe** 268×38 / 300×42: logo 62–80 px, valore 16–17 px, FINO A 10 px |
| P5 | Importo "5.200€" nella riga (colonna valore) | 300×250 | colonna 62 px, testo 61,1 px a 16 px: entra senza tagli; testo allineato a destra su tutte le righe, quindi le cifre sono a filo |
| P6 | Wipe orizzontale su 300 px: troppo rapido | 300×250, 336×280 | stessa durata 0,30 s, banda 120–130 px (40 % della larghezza): leggibile come "passaggio di luce", non come flash |
| P7 | CTA durante i morph vicino alle card (S5 sale dal basso) | 300×250, 336×280 | salita delle righe S5 ridotta a 4 px; gap minimo visibile 6,8 / 8,8 px (misurato a passo 20 ms) |
| P8 | Safe area: fascia da 108 px su 1920 è alta | 1920×1080 | 10 % dell'altezza (regola di famiglia: ≥ 10 % e ≥ 30 px); a 1080p 108 px ospita due righe di dicitura a 36 px |
| P9 | Particelle e flare a 1920 devono restare discrete | 1920×1080 | 40 particelle da 5 px, flare 1600×1100 in alto a sinistra con decadimento a 0,38 |
| P10 | Durata: 10 s (famiglia) o 12 s (master) per il 16:9 | 1920×1080 | storyboard a 10 s per coerenza di famiglia e riuso dell'audio; alternativa 12 s = timeline del master, da decidere al gate |

## 2.5 Zone di movimento / zone libere
Movimento: titolo, hero, card, CTA (solo lungo l'asse x = W/2), wipe (area utile), camera (deriva ≤ 14 px su 1920, ≤ 2 px sui rettangoli), particelle (y < usable − 12). Libere: fascia disclaimer piatta `#061a12` (1920×108 · 300×30 · 336×34), margini laterali.
