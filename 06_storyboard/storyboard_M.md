# Storyboard — Concept M "Montaggio a scene" · 970×250 · 25 fps · 12,0 s · 300 fotogrammi · con SFX (mai voiceover)

Stato: **in attesa di approvazione esplicita**. Fotogrammi reali renderizzati dal progetto `08_progetto/banner_scene.html` (ambiente Higgsfield definitivo). `frames_M/` = con safe area evidenziata in magenta (solo per lettura); `frames_M_clean/` = come apparirà. Contact sheet: `storyboard_M_contact_sheet.png`.

Convenzione: f = t × 25; f0 = primo fotogramma; f299 = ultimo (t = 11,96 s); il file dura esattamente 12,00 s.

## 1. Timeline

| t (s) | f | Blocco | Che cosa accade | Statico | Animato |
|---|---|---|---|---|---|
| 0,00 | 0 | S1 | Fondo verde-nero. **La CTA è già in quadro** (grande, a destra, scala 0,6→1 in 0,45 s). Safe area vuota | safe | CTA (arrivo), ambiente (dissolvenza 0–0,7 s) |
| 0,25–1,08 | 6–27 | S1 | "BONUS" (bianco) poi "SPORT" (lime) si rivelano da maschera, tracking 0,14 em → −0,01 em; ambiente si accende (flare, raggi) | CTA, safe | titolo, ambiente |
| 0,95–1,25 | 24–31 | S1 | I due punti compaiono (scala 0,4→1): "BONUS SPORT:" | titolo | ":" |
| 1,10–1,60 | 27–40 | S1 | Regolo lime si estende sotto il titolo (427 px) | titolo, CTA | regolo |
| 1,25–1,85 | 31–46 | S1 | Passaggio di luce diagonale attraversa il titolo | tutto | luce |
| 1,70–2,20 | 42–55 | S1 | Riflesso sulla CTA grande | tutto | riflesso |
| 2,20–2,60 | 55–65 | S1 | **Fermo di lettura** "BONUS SPORT: SCOPRI DI PIÙ" | tutto | ambiente (deriva) |
| 2,50–3,05 | 62–76 | T1 | **La CTA migra** da (607,79) 230×52 a (800,83) 150×44 con un morph continuo: non esce mai dal quadro | — | CTA |
| 2,60–2,95 | 65–74 | T1 | **Wipe di luce**: S1 esce da sinistra, S2 entra; banda luminosa inclinata da −120 px a +1010 px; cambio di camera | safe, CTA | tutto |
| 2,95–4,80 | 74–120 | S2 Sisal | Etichetta "BONUS SPORT" piccola a sinistra (0,05–0,45 s); **hero card** (335,30) 300×158 sale con rotateX 14°→0 e blur 5→0 (0–0,50 s); logo Sisal 172 px in dissolvenza e scala 0,94→1 (0,30–0,70 s); indice "1 / 3" (0,50–0,80 s); "FINO A" (0,60–0,85 s); cifre di **5.200€** una alla volta, tutte complete a **1,15 s** (t=4,10); riflesso vetro (1,25–1,75 s); fermo fino a 1,85 s | CTA, safe, etichetta | card, logo, valore, riflesso |
| 4,80–5,10 | 120–128 | T2 | Wipe di luce identico a T1 | CTA, safe | tutto |
| 5,10–6,95 | 128–174 | S3 NetBet | **Stessa coreografia e stessi tempi di S2**, logo NetBet 164 px, indice "2 / 3", valore **1.000€** completo a t=6,25 | idem | idem |
| 6,95–7,25 | 174–181 | T3 | Wipe di luce identico | CTA, safe | tutto |
| 7,25–9,10 | 181–228 | S4 William Hill | **Stessa coreografia e stessi tempi**, logo William Hill 202 px, indice "3 / 3", valore **255€** completo a t=8,40 | idem | idem |
| 9,10–9,45 | 228–236 | T4 | Wipe di luce identico, camera torna a 1,00 | CTA, safe | tutto |
| 9,25–10,20 | 231–255 | S5 | **Comparazione**: "BONUS"/"SPORT" a sinistra (37 px) si rivelano da maschera; **le tre card entrano insieme** (0,05–0,75 s dalla scena: salita 28 px, rotateX 16°→0, blur 5→0), con loghi e valori già completi (già mostrati uno per uno); regolo lime | CTA, safe | titolo, card |
| 10,20–10,70 | 255–268 | S5 | Fermo di confronto: 5.200€ · 1.000€ · 255€ stessa dimensione, stessa baseline | tutto | ambiente |
| 10,70–11,30 | 268–283 | S6 | **Enfasi CTA**: scala 1→1,12 (0,6 s) poi assestamento a 0,97 (0,5 s); anello che si espande e svanisce (0,8 s); alone radiale (1,3 s, poi resta al 35 %); secondo riflesso (11,10–11,70) | titolo, card, safe | CTA |
| 11,80–12,00 | 295–299 | S6 | **End frame** stabile: titolo, tre card, CTA in risalto, safe area vuota. Usabile come fallback statico | tutto | — |

Durata utile in cui **tutte** le informazioni (tre loghi + tre valori) sono contemporaneamente leggibili: 10,20–12,00 s (1,8 s) in S5, oltre ai 0,7 s di fermo di ciascun operatore in S2–S4. Se il cliente vuole più tempo di confronto, la variante a 13,0 s aggiunge 0,5 s a S1 e 0,5 s a S5.

## 2. Layout per scena (px, origine in alto a sinistra)

| Scena | Elemento | x, y | w × h | Note |
|---|---|---|---|---|
| S1 | "BONUS" | 132, 72 | 212 × 66 | Montserrat 800, 56 px, bianco |
| S1 | "SPORT" | 362, 72 | 197 × 66 | lime `#b9d531` |
| S1 | ":" | 561, 66 | 16 × 66 | lime; opzionale |
| S1 | CTA grande | 607, 79 | 230 × 52 | pill lime, testo `#06301d` 20 px |
| S1 | regolo | 132, 150 | 427 × 2 | lime |
| S2–S4 | etichetta "BONUS SPORT" | 26, 96 | — | 16 px, 90 % opacità |
| S2–S4 | hero card | 335, 30 | 300 × 158 | raggio 14; identica per i tre |
| S2–S4 | logo-box | +0, +22 | 300 × 56 | Sisal 172 · NetBet 164 · William Hill 202 px (stesso rapporto di equalizzazione ottica del concept A, ×1,45); proporzioni intatte |
| S2–S4 | "FINO A" / valore | +0, +86 / +0, +104 | — | Inter 600 12 px / Montserrat 800 38 px, cifre tabulari; identico per i tre |
| S2–S4 | indice "n / 3" | in alto a destra nella card | — | Inter 600 10,5 px, 90 % |
| S5/S6 | titolo | 26, 60 | 196 × 92 | come concept A |
| S5/S6 | card | 232 / 420 / 608, 32 | 168 × 146 | identiche; loghi 118/112/138 px; valori 29 px |
| tutte | CTA (dopo T1) | 800, 83 | 150 × 44 | 13,5 px; in S6 scala fino a 1,12 → 0,97 (resta dentro 780–970 × 60–150) |
| **tutte** | **Safe area disclaimer** | **0, 210** | **970 × 40** | **piatta `#061a12`, nessun elemento, nessun movimento, nessun wipe, per tutti i 300 fotogrammi** |

I wipe e gli effetti di luce sono confinati a y < 210: la safe area non viene mai attraversata.

## 3. Sequenza per fotogramma-chiave (le 16 immagini)

| # | t | f | Immagine | Scena | Descrizione |
|---|---|---|---|---|---|
| 01 | 0,00 | 0 | `scena_01_t0.00s` | S1 | Apertura: solo CTA (grande, in arrivo) su fondo scuro |
| 02 | 0,60 | 15 | `scena_02_t0.60s` | S1 | "BONUS" e "SPORT" in risalita, ambiente si accende |
| 03 | 1,20 | 30 | `scena_03_t1.20s` | S1 | "BONUS SPORT:" completo con CTA grande; regolo in estensione |
| 04 | 1,65 | 41 | `scena_04_t1.65s` | S1 | Passaggio di luce sul titolo |
| 05 | 2,40 | 60 | `scena_05_t2.40s` | S1 | Fermo di lettura |
| 06 | 2,78 | 70 | `scena_06_t2.78s` | T1 | Wipe di luce a metà; la CTA sta migrando a destra e riducendosi |
| 07 | 3,30 | 82 | `scena_07_t3.30s` | S2 | Hero card Sisal in arrivo, logo in dissolvenza, etichetta a sinistra |
| 08 | 4,20 | 105 | `scena_08_t4.20s` | S2 | Sisal · FINO A 5.200€ completo, riflesso vetro, indice 1/3 |
| 09 | 4,95 | 124 | `scena_09_t4.95s` | T2 | Wipe; CTA presente |
| 10 | 6,50 | 162 | `scena_10_t6.50s` | S3 | NetBet · FINO A 1.000€, indice 2/3 (stessa coreografia) |
| 11 | 7,10 | 178 | `scena_11_t7.10s` | T3 | Wipe |
| 12 | 8,60 | 215 | `scena_12_t8.60s` | S4 | William Hill · FINO A 255€, indice 3/3 (stessa coreografia) |
| 13 | 9,28 | 232 | `scena_13_t9.28s` | T4 | Wipe verso la comparazione; "BONUS" di S5 già in arrivo |
| 14 | 10,10 | 252 | `scena_14_t10.10s` | S5 | Comparazione completa: tre card identiche, valori allineati |
| 15 | 11,00 | 275 | `scena_15_t11.00s` | S6 | Enfasi CTA: scala, anello, alone |
| 16 | 12,00 | 300 | `scena_16_t12.00s` | S6 | End frame stabile (fallback statico) |

## 4. Gerarchia di lettura e ruolo di Sisal
- S1: 1. "BONUS SPORT" 2. CTA. — S2–S4: 1. logo 2. valore 3. CTA 4. etichetta. — S5/S6: 1. i tre valori 2. i tre loghi 3. CTA (in risalto) 4. titolo.
- Sisal: primo della sequenza (ordine richiesto, coincidente con il criterio decrescente), stessa inquadratura/durata degli altri; il lime del suo logo colora CTA e accenti tipografici, condivisi da tutto il banner. Nessun accento esclusivo sulla sua card in S5 (opzionale).

## 5. Transizioni (T1–T4)
Wipe di luce: la scena uscente viene mascherata da sinistra (`clip-path inset`), quella entrante rivelata da sinistra; sopra scorre una banda luminosa bianca-lime inclinata (larghezza 120 px, opacità a campana). Durata 0,30–0,35 s, easing in-out. Il cambio di camera (scala/posizione dell'ambiente) avviene sotto la banda, così il taglio è percepito come un vero stacco tra clip diverse e non come un pannello che scorre. La CTA non fa parte dei layer mascherati: sta su un layer superiore ed è continua.

## 6. Piano audio (novità rispetto al brief: il cliente ha chiesto SFX; il brief originario "senza audio" è superato per MP4 master/web)

**Regole**: mai voiceover, mai voce sintetica, mai musica con voce, mai testo parlato o cantato. Nessun modello TTS/voce viene invocato. La traccia è composta da soli effetti e ambiente.

### 6.1 Verifica di ciò che Higgsfield MCP può fare per l'audio (fatta il 2026-09-10)
`generate_audio`/`generate_audio_batch` sono strumenti **solo text-to-speech** (seed_audio, text2speech_v2, qwen_audio_tts): la descrizione ufficiale dello strumento dichiara che non può generare musica o sound effect per uso generale e che i modelli `mirelo_text_to_audio` (SFX) e `sonilo_music` esistono **solo per la pipeline di generazione giochi** e non vanno usati per audio autonomo. Quindi: **Higgsfield non viene usato per SFX/ambiente**, e ovviamente non per voci (vietate dal cliente). I modelli video con audio nativo (veo3_1, seedance con `generate_audio:true`) produrrebbero picture+audio generativi non deterministici: esclusi.

### 6.2 Sorgente proposta: sintesi procedurale nel progetto (deterministica, senza diritti di terzi)
Script Python (numpy + ffmpeg, seme fisso) in `08_progetto/audio/` che genera:

| Cue | t (s) | Descrizione | Livello indicativo |
|---|---|---|---|
| Bed "stadio lontano" | 0,00–12,00 | rumore rosa/marrone filtrato (200 Hz–3 kHz), modulazione lenta simile a un brusio di folla distante, leggero riverbero; fade-in 0,7 s (con l'ambiente), fade-out 0,6 s | −30 LUFS circa (sotto tutto) |
| Accensione | 0,10–1,60 | crescendo tenue (l'ambiente "si accende") | −28 dBFS picco |
| Whoosh T1 | 2,55–3,00 | rumore bianco filtrato passa-banda con sweep 400 Hz → 4 kHz, inviluppo a campana, leggero pan L→R (segue la banda di luce) | −14 dBFS picco |
| Whoosh T2 / T3 / T4 | 4,78–5,12 · 6,93–7,27 · 9,08–9,47 | identico a T1 (stesso campione) | idem |
| "Lock" valore | 4,10 · 6,25 · 8,40 | tick morbido (impulso breve + coda 80 ms) quando le cifre si completano: **stesso suono, stesso livello per i tre operatori** | −18 dBFS picco |
| Card S5 | 9,50–10,20 | soffio breve in arrivo delle tre card (unico, non tre) | −20 dBFS picco |
| CTA S6 | 10,70 | "ping" corto (seno 880 Hz + armonica, decadimento 350 ms) + soffio dell'anello | −16 dBFS picco |
| Riflessi vetro | 4,20 · 6,35 · 8,50 | shimmer tenuissimo (opzionale) | −26 dBFS |

Mix: 48 kHz, stereo; loudness integrata target **−20 LUFS** (banner display: udibile ma non invadente), true-peak ≤ −1 dBTP; nessun evento audio dopo 11,70 s (coda pulita per il loop/fine). Formato di consegna: AAC 128 kbps nel MP4 master/web; WAV 48 kHz 24 bit separato in `10_export/audio/` per eventuali sostituzioni.

### 6.3 Alternativa
Se il cliente dispone di una libreria SFX licenziata (o preferisce suoni "reali" di stadio), i file vengono montati **nelle stesse posizioni e agli stessi livelli** della tabella; lo script di mix è lo stesso. Non uso librerie non licenziate né estraggo audio da video di terzi.

### 6.4 Consegne audio/muto
- `…_MASTER.mp4` e `…_WEB.mp4` **con audio**; `…_WEB_MUTO.mp4` senza traccia (per i circuiti che vietano l'audio o per autoplay muto); GIF muta per natura. La comprensione del banner **non dipende dall'audio**: tutte le informazioni sono visive.

## 7. Piano QC specifico per il concept M (in aggiunta a `11_qc/piano_qc.md`)
1. CTA presente e integra in **ogni** fotogramma, con posizione attesa variabile nel tempo (grande a 607,79 fino a 2,50 s; morph 2,50–3,05; piccola a 800,83 poi; scala S6): il controllo campiona la pill nella posizione calcolata dalla stessa funzione del template.
2. Safe area piatta in tutti i 300 fotogrammi anche **durante i wipe** (nessuna banda di luce sotto y=210).
3. Pari trattamento sequenziale: per S2/S3/S4 gli istanti di inizio/fine di hero, logo, "FINO A", cifre complete e riflesso devono essere identici in tempo relativo (verifica sulle costanti del template + diff dei fotogrammi ai tempi omologhi: uguale luminanza media della card, uguale altezza del valore).
4. Loghi: nessuna deformazione (rapporto larghezza/altezza uguale al file ufficiale ±0,5 %), nessun patch dietro; posizione stabile nel fermo di ogni clip e in S5.
5. Valori: stringhe DOM esattamente "5.200€", "1.000€", "255€" (letti dal template, non da OCR) e stessa dimensione font per i tre.
6. Audio: nessuna voce (analisi spettrale: assenza di formanti/energia vocale nella banda 300 Hz–3 kHz correlata a modulazione sillabica; controllo d'ascolto), loudness −20 LUFS ±1, true-peak ≤ −1 dBTP, eventi ai tempi della tabella (±1 frame), fine audio ≤ 11,70 s; `…_WEB_MUTO.mp4` senza stream audio.
7. Pesi: web MP4 ≤ 3,5 MB con audio; GIF ≤ 3,5 MB (300 fotogrammi: ambiente fermo, palette per scena; se supera, 12,5 fps).

## 8. Ruolo di Higgsfield MCP nel concept M
- **Ambiente**: già generato e selezionato (job `b8ed1902…`, nano_banana_2), riutilizzato; nessuna nuova generazione necessaria. Se il cliente vuole un ambiente diverso per le scene operatore (es. una variante più scura), 1 batch di 4 still ≈ 8 crediti.
- **Audio**: non utilizzabile per SFX/ambiente (vedi §6.1); mai per voce.
- **Testi, loghi, importi, €, CTA, disclaimer**: mai generati (vincolo del brief).

## 9. Che cosa succede dopo l'approvazione
1. Conferma di: durata (12 o 13 s), due punti sì/no, accento S5 sì/no, sorgente audio (procedurale o libreria del cliente), bed stadio sì/no.
2. Produzione: render 2× dei 300 fotogrammi, sintesi e mix audio, encoding master/web/muto/GIF, QC automatico + visivo, report.
3. Consegna in `10_export/` con nomi `BonusSport_970x250_25fps_12s_M_*`; il concept A resta disponibile.
