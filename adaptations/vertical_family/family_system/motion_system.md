# Sistema di movimento della famiglia verticale (10,0 s · 25 fps · 250 fotogrammi · senza audio)

## Struttura temporale (derivata dal master 12 s, compressa a 10 s senza cambiare la funzione narrativa)

| Blocco | Master (s) | Verticali (s) | Fotogrammi | Funzione narrativa (invariata) |
|---|---|---|---|---|
| S1 titolo | 0,00–2,60 | 0,00–2,00 | 0–49 | "BONUS" → "SPORT" → regolo → CTA (ordine approvato) |
| T1 wipe | 2,60–2,95 | 2,00–2,30 | 50–57 | passaggio di luce, la CTA morfa da grande a media |
| S2 Sisal | 2,95–4,80 | 2,30–3,80 | 58–94 | hero card: card → logo → FINO A → cifre |
| T2 | 4,80–5,10 | 3,80–4,10 | 95–102 | wipe |
| S3 NetBet | 5,10–6,95 | 4,10–5,60 | 103–139 | come S2, stessa clip |
| T3 | 6,95–7,25 | 5,60–5,90 | 140–147 | wipe |
| S4 William Hill | 7,25–9,10 | 5,90–7,40 | 148–184 | come S2 |
| T4 | 9,10–9,45 | 7,40–7,70 | 185–192 | wipe, CTA morfa verso la posizione finale |
| S5 confronto | 9,45–12,00 | 7,70–10,00 | 193–249 | titolo + tre card insieme, hold, due pulse CTA |
| CTA in | 1,10–1,55 | 0,90–1,30 | 23–32 | terza a entrare in S1 |
| Morph 1 | 2,50–3,05 | 1,90–2,40 | 48–60 | grande → media |
| Morph 2 | 9,05–9,50 | 7,25–7,70 | 181–192 | media → confronto: la CTA è ferma nella posizione finale quando le card di S5 arrivano |
| Pulse 1 / 2 | 10,70 / 11,45 | 8,90 / 9,55 | 223–236 / 239–249 | ampiezza 9 % + 6 % (160×600: 7 % + 5 %) |

Hold minimi rispettati: ogni scena operatore resta ferma con dati completi per ≥ 0,55 s (master 0,70 s); S5 hold con tutto a fuoco ≥ 1,55 s; ultimo fotogramma = stato finale completo (fallback statico).

## Movimenti (stessa libreria di easing del master: eoE, eoC, eio, eioC, eoQ)
- **Titolo S1**: parole in slide-up da clip (104 % → 0), tracking 0,14 → −0,01 em, BONUS 0,20–0,80 s, SPORT 0,38–0,98 s; regolo lime cresce dal centro 0,90–1,30 s. Identico al master, solo impilato.
- **CTA**: unica, mai mascherata dai wipe; entra in scala 0,7 → 1 con traslazione 18 px; morph di posizione/dimensione/corpo in easing cubico in-out. Il percorso di morph è **verticale** (scende lungo l'asse) invece che orizzontale: stessa funzione (la CTA "segue" il blocco contenuti).
- **Card operatore** (clip relativa alla scena): card 0–0,42 s (rise 26 px, rotateX 14° → 0, blur 5 → 0), logo 0,25–0,58 s (scala 0,94 → 1), FINO A 0,50–0,70 s, cifre 0,59–0,95 s (roll-up 40 px per cifra, sfalsamento 30 ms). Stessa sequenza del master, tempi ridotti del 17 %.
- **Wipe**: nel master la banda di luce attraversa da sinistra a destra (skew −14°); nelle verticali la banda **scende** dall'alto (skew −6°, altezza 120 px) e le scene sono mascherate con `clip-path` alto/basso. La banda esiste solo dentro l'area utile (da −120 a usable + 120 con opacità sinusoidale: a fine corsa è già a opacità 0 quando tocca y = usable — verificato: fascia piatta su tutti i campioni).
- **S5**: titolo slide-up (0,15 s di anticipo come master), regolo, card che entrano insieme con sfalsamento 60 ms, salita 12 px (ridotta dai 24 px del master perché nelle verticali la CTA sta sotto le card), dati già visibili (nessun rollo delle cifre: come master).
- **Camera sull'ambiente**: deriva −8 px / scala 1,03 → 1,00 lungo i 10 s + offset per scena (S1 1,06 · Sisal −6 px 1,02 · NetBet +5 px 1,03 · WH −3 px 1,04 · S5 1,00), stessa logica di "respiro" del master; particelle 14 / 12 / 8 con deriva verticale lenta, confinate a y < usable − 12.
- **Pulse finale**: solo scala della CTA (origine al centro), nessun anello/alone (decisione rev 2 del master).

## Zone di movimento / zone libere
- Zona di movimento: l'intera area utile meno i margini; la CTA si muove solo lungo l'asse centrale.
- Zona libera assoluta: fascia disclaimer (y ≥ usable) — nessun elemento, luce, particella o ombra vi entra. L'ombra della CTA (22 px di blur) resta ≥ 24 px sopra la fascia (≥ 26 su 320×480 con box a 404: l'ombra sfuma a 0 entro 418).
