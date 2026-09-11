# Sistema di movimento della famiglia orizzontale (10,0 s · 25 fps · 250 fotogrammi · con audio)

## Struttura temporale (identica alla famiglia verticale, derivata dal master 12 s)

| Blocco | Master (s) | Orizzontali (s) | Fotogrammi | Funzione |
|---|---|---|---|---|
| S1 titolo | 0,00–2,60 | 0,00–2,00 | 0–49 | "BONUS" → "SPORT" → regolo → CTA |
| T1 wipe | 2,60–2,95 | 2,00–2,30 | 50–57 | banda di luce sinistra → destra, CTA morfa grande → media |
| S2 Sisal | 2,95–4,80 | 2,30–3,80 | 58–94 | hero: card → logo → FINO A → cifre |
| T2 | 4,80–5,10 | 3,80–4,10 | 95–102 | wipe |
| S3 NetBet | 5,10–6,95 | 4,10–5,60 | 103–139 | come S2 |
| T3 | 6,95–7,25 | 5,60–5,90 | 140–147 | wipe |
| S4 William Hill | 7,25–9,10 | 5,90–7,40 | 148–184 | come S2 |
| T4 | 9,10–9,45 | 7,40–7,70 | 185–192 | wipe, CTA morfa verso la posizione finale |
| S5 confronto | 9,45–12,00 | 7,70–10,00 | 193–249 | titolo + tre card/righe insieme, hold, due pulse |
| CTA in | 1,10–1,55 | 0,90–1,30 | 23–32 | |
| Morph 1 / 2 | 2,50–3,05 / 9,05–9,50 | 1,90–2,40 / 7,25–7,70 | 48–60 / 181–192 | la CTA è ferma quando arrivano le card di S5 |
| Pulse 1 / 2 | 10,70 / 11,45 | 8,90 / 9,55 | 223–236 / 239–249 | 9 % + 6 % (tutte le size: i bordi non sono mai toccati) |

Hold: scene operatore con dati completi ≥ 0,55 s; S5 ≥ 1,55 s; ultimo fotogramma = stato finale completo.

## Movimenti
- **Titolo S1**: le due parole su una riga entrano in slide-up da clip con tracking 0,14 → −0,01 em (BONUS 0,20–0,80, SPORT 0,38–0,98), regolo dal centro 0,90–1,30: identico al master.
- **CTA**: unica, entra in scala 0,7 → 1 con traslazione; morph verticale lungo l'asse (S1 → hero → S5) in easing cubico in-out; pulse finale solo di scala.
- **Hero card**: card 0–0,42 s (salita 15 % dell'altezza: 75 / 18 / 20 px, rotateX 14° → 0, blur 5 → 0), logo 0,25–0,58, FINO A 0,50–0,70, cifre 0,59–0,95 (roll-up).
- **Wipe**: come il master, banda skew −14° che attraversa da sinistra a destra in 0,30 s (larghezza 280 / 120 / 130 px), scene mascherate con `clip-path` sinistra/destra; la banda è alta quanto l'area utile (+ 60 px sopra) e non entra nella fascia disclaimer (verificato: fascia piatta su 50 campioni per size).
- **S5**: titolo slide-up con anticipo 0,15 s, regolo, card che entrano insieme con sfalsamento 60 ms; salita 48 px su 1920 (card 400 px), **4 px** sulle righe dei rettangoli (per non avvicinarsi alla CTA); dati già visibili.
- **Camera**: deriva orizzontale del master scalata per larghezza (14 px × W/1920) + offset per scena (S1 1,06 · Sisal −6 1,02 · NetBet +5 1,03 · WH −3 1,04 · S5 1,00); particelle 40 (5 px) / 8 / 8 confinate a y < usable − 12.

## Audio (sempre presente)
Stessa traccia del master ri-temporizzata: profilo `vertical` (10 s) di `08_progetto/audio/make_audio.py` — bed stadio reale (clip Higgsfield `9d228081…`) + soffi 0,20 / 0,38 / 0,90, whoosh 2,00 / 3,80 / 5,60 / 7,40, tick 3,25 / 5,05 / 6,85, soffio S5 7,75, ping 8,90 / 9,45, fade 9,90. Per gli orizzontali il wipe va da sinistra a destra come nel master: in produzione il profilo viene clonato come `horizontal` con `pan_sweep=True` (panoramica L→R sui whoosh), unica differenza. −20 LUFS, TP ≤ −1 dBTP, ultimo evento ≤ 9,95 s. Consegna: MASTER.mp4 e WEB.mp4 con AAC, archivio 4:4:4 PCM 24 bit, WEB_MUTO.mp4 come extra.

## Opzione 12 s per il 1920×1080 (da decidere al gate)
Il 16:9 è l'unico formato "video" della famiglia: può usare la timeline del master (12 s, profilo audio `master` con pan sweep) invece dei 10 s di famiglia. Costo: nessuno (parametro `--duration 12` + tabella tempi del master); vantaggio: hold più lunghi sulle cifre (0,70 s) e S5 di 2,55 s. Lo storyboard consegnato è a 10 s per coerenza con i rettangoli; se si sceglie 12 s, lo storyboard 1920 viene rigenerato prima della produzione.
