# Storyboard — Concept M "Montaggio a scene" · v2 · 970×250 · 25 fps · 12,0 s · 300 fotogrammi · con SFX (mai voiceover)

Stato: **v2 APPROVATA e prodotta** (2026-09-10). Conferme del cliente: sfondo zenitale ok · 12,0 s · audio ok (bed stadio + SFX procedurali) · nessun accento sulla card Sisal in S5 · **indici "1/3, 2/3, 3/3" rimossi dalle card** (unica differenza rispetto ai fotogrammi dello storyboard). Esportazioni in `10_export/` (prefisso `BonusSport_970x250_25fps_12s_M_`), QC in `11_qc/report_qc_M.md`. Fotogrammi reali renderizzati dal progetto `08_progetto/banner_scene.html`. `frames_M/` = con safe area evidenziata in magenta (solo per lettura); `frames_M_clean/` = come apparirà. Contact sheet: `storyboard_M_contact_sheet.png`.

## 0-bis. Revisione 2 dopo la prima consegna (note del cliente → soluzione)

| Nota | Soluzione |
|---|---|
| Effetto "vetro" eccessivo | Rimossi tutti i riflessi diagonali (sulle hero card, sul titolo di S1, sulla CTA); card più solide (fondo 80 % invece di 42 %, senza gradiente bianco); raggi e flare dei riflettori attenuati. Restano solo i wipe di luce delle transizioni |
| Sound effect brutto, rumore continuo non da stadio | Bed sostituito con un **ambiente stadio reale** estratto da una clip Higgsfield con audio nativo (veo3_1, job 9d228081…, nessun parlato verificato con trascrizione automatica); whoosh più corti e 5 dB più bassi, tick e ping più discreti; nessuna voce |
| Anello attorno alla CTA finale distorto | **Anello e alone eliminati**: l'enfasi finale è solo un pulse del tasto (due battiti morbidi, +9 % e +6 %, ancorati al bordo destro) |

## 0. Che cosa cambia nella v2 (note del cliente → soluzione)

| Nota | Soluzione nella v2 |
|---|---|
| Eliminare i due punti dopo "SPORT" | Rimossi. S1 legge "BONUS SPORT  SCOPRI DI PIÙ"; titolo e CTA ricentrati sull'intero formato |
| L'etichetta piccola "BONUS SPORT" nelle scene operatore è troppo piccola: ingrandirla o toglierla | **Tolta**: il titolo è già stato dato in S1 e torna in S5. Le scene operatore restano pulite: hero card + CTA |
| Al massimo, l'ingresso di S1 sia: BONUS, poi SPORT, poi la CTA | Fatto: "BONUS" 0,25–0,95 s → "SPORT" 0,45–1,15 s → CTA 1,10–1,55 s (entra da destra, scala 0,7→1). Dalla sua entrata la CTA resta in quadro fino all'ultimo fotogramma |
| La CTA nelle scene operatore deve essere più grande e meglio posizionata | CTA **media** 210×54 (18 px) a (565,80), accanto alla hero card: card e CTA formano un gruppo centrato (195–775 su 970), allineato verticalmente al centro della card. Morph continuo: grande (S1) → media (S2–S4) → piccola (S5), mai fuori quadro |
| Manca uno sfondo di calcio: si vede solo un verde petrolio | Nuovo ambiente Higgsfield: **campo di calcio visto dall'alto** (cerchio di centrocampo al centro, linee bianche sottili, notturno), tinto nel verde Sisal e attenuato (ombra centrale morbida, vignetta), così gli elementi grafici restano in primo piano. Nessun elemento IP |

## 1. Timeline

| t (s) | f | Blocco | Che cosa accade | Statico | Animato |
|---|---|---|---|---|---|
| 0,00–0,70 | 0–17 | S1 | Il campo visto dall'alto emerge in dissolvenza; riflettori "si accendono" (flare 0,10–0,55, raggi 0,30–1,40) | safe | ambiente |
| 0,25–0,95 | 6–24 | S1 | **"BONUS"** (bianco, 56 px) si rivela da maschera, tracking 0,14 em → −0,01 em | safe | titolo |
| 0,45–1,15 | 11–29 | S1 | **"SPORT"** (lime) segue con la stessa animazione | "BONUS" | titolo |
| 1,10–1,55 | 27–39 | S1 | **La CTA grande** (230×52) entra per terza: da destra (36 px), scala 0,7→1, opacità 0→1 | titolo | CTA |
| 1,10–1,60 | 27–40 | S1 | Regolo lime si estende sotto il titolo (427 px) | titolo | regolo |
| 2,20–2,60 | 55–65 | S1 | **Fermo di lettura** "BONUS SPORT  SCOPRI DI PIÙ" | tutto | ambiente (deriva) |
| 2,50–3,05 | 62–76 | T1 | **Morph 1 della CTA**: da (599,79) 230×52 a (565,80) 210×54; non esce mai dal quadro | — | CTA |
| 2,60–2,95 | 65–74 | T1 | **Wipe di luce**: S1 esce da sinistra, S2 entra; cambio di camera (scala 1,06 → 1,02, −28 px) | safe, CTA | tutto |
| 2,95–4,80 | 74–120 | S2 Sisal | **Hero card** (195,30) 300×158 sale con rotateX 14°→0 e blur 5→0 (0–0,50 s); logo Sisal 172 px in dissolvenza e scala 0,94→1 (0,30–0,70 s); indice "1 / 3" (0,50–0,80 s); "FINO A" (0,60–0,85 s); cifre di **5.200€** una alla volta, complete a **1,15 s** (t=4,10); fermo fino a 1,85 s (riflesso vetro rimosso nella revisione 2). CTA media ferma a destra della card | CTA, safe | card, logo, valore, riflesso |
| 4,80–5,10 | 120–128 | T2 | Wipe di luce identico a T1 | CTA, safe | tutto |
| 5,10–6,95 | 128–174 | S3 NetBet | **Stessa coreografia e stessi tempi di S2**, logo NetBet 164 px, indice "2 / 3", valore **1.000€** completo a t=6,25 | idem | idem |
| 6,95–7,25 | 174–181 | T3 | Wipe di luce identico | CTA, safe | tutto |
| 7,25–9,10 | 181–228 | S4 William Hill | **Stessa coreografia e stessi tempi**, logo William Hill 202 px, indice "3 / 3", valore **255€** completo a t=8,40 | idem | idem |
| 9,05–9,50 | 226–238 | T4 | **Morph 2 della CTA**: da media a piccola (800,83) 150×44 | — | CTA |
| 9,10–9,45 | 228–236 | T4 | Wipe di luce identico, camera torna a 1,00 | CTA, safe | tutto |
| 9,25–10,20 | 231–255 | S5 | **Comparazione**: "BONUS"/"SPORT" a sinistra (37 px) si rivelano da maschera; **le tre card entrano insieme** (salita 28 px, rotateX 16°→0, blur 5→0), con loghi e valori già completi; regolo lime | CTA, safe | titolo, card |
| 10,20–10,70 | 255–268 | S5 | Fermo di confronto: 5.200€ · 1.000€ · 255€ stessa dimensione, stessa baseline | tutto | ambiente |
| 10,70–11,85 | 268–296 | S6 | **Pulse CTA**: due battiti morbidi del tasto (10,70–11,25: +9 %; 11,45–12,00: +6 %), ancorati al bordo destro; nessun anello, nessun alone, nessun riflesso (revisione 2) | titolo, card, safe | CTA |
| 11,80–12,00 | 295–299 | S6 | **End frame** stabile: titolo, tre card, CTA in risalto, safe area vuota. Usabile come fallback statico | tutto | — |

Presenza della CTA: assente solo nei primi 1,10 s di S1 (ingresso BONUS → SPORT → CTA richiesto dal cliente), poi **presente e integra in ogni fotogramma** fino a 12,00 s, attraversando tutte le transizioni. Durata in cui tutte le informazioni (tre loghi + tre valori) sono contemporaneamente leggibili: 10,20–12,00 s (1,8 s) in S5, oltre ai 0,7 s di fermo di ciascun operatore in S2–S4. La variante a 13,0 s aggiungerebbe 0,5 s a S1 e 0,5 s a S5.

## 2. Layout per scena (px, origine in alto a sinistra)

| Scena | Elemento | x, y | w × h | Note |
|---|---|---|---|---|
| S1 | "BONUS" | 142, 72 | 212 × 66 | Montserrat 800, 56 px, bianco |
| S1 | "SPORT" | 372, 72 | 197 × 66 | lime `#b9d531`; gap 18 px da "BONUS" |
| S1 | CTA grande | 599, 79 | 230 × 52 | pill lime, testo `#06301d` 20 px; gap 30 px dal titolo; gruppo titolo+CTA centrato (142–829) |
| S1 | regolo | 142, 150 | 427 × 2 | lime |
| S2–S4 | hero card | 195, 30 | 300 × 158 | raggio 14; identica per i tre |
| S2–S4 | logo-box | +0, +22 | 300 × 56 | Sisal 172 · NetBet 164 · William Hill 202 px (stesso rapporto di equalizzazione ottica del concept A, ×1,45); proporzioni intatte |
| S2–S4 | "FINO A" / valore | +0, +86 / +0, +104 | — | Inter 600 13 px / Montserrat 800 38 px, cifre tabulari; identico per i tre |
| S2–S4 | indice "n / 3" | in alto a destra nella card | — | Inter 600 10 px, 45 % |
| S2–S4 | CTA media | 565, 80 | 210 × 54 | 18 px; centro verticale allineato alla card; gruppo card+CTA centrato (195–775) |
| S5/S6 | titolo | 26, 60 | 196 × 92 | come concept A |
| S5/S6 | card | 232 / 420 / 608, 32 | 168 × 146 | identiche; loghi 118/112/138 px; valori 29 px |
| S5/S6 | CTA piccola | 800, 83 | 150 × 44 | 13,5 px; in S6 scala fino a 1,12 → 0,97 **ancorata al bordo destro** (x=950 fisso, cresce verso sinistra); anello e alone entro x=950 |
| **tutte** | **Safe area disclaimer** | **0, 210** | **970 × 40** | **piatta `#061a12`, nessun elemento, nessun movimento, nessun wipe, per tutti i 300 fotogrammi** |

I wipe e gli effetti di luce sono confinati a y < 210: la safe area non viene mai attraversata.

## 3. Sequenza per fotogramma-chiave (le 16 immagini)

| # | t | f | Immagine | Scena | Descrizione |
|---|---|---|---|---|---|
| 01 | 0,35 | 9 | `scena_01_t0.35s` | S1 | Apertura: "BONUS" in risalita sul campo visto dall'alto |
| 02 | 0,75 | 19 | `scena_02_t0.75s` | S1 | "BONUS" fermo, "SPORT" in arrivo |
| 03 | 1,30 | 33 | `scena_03_t1.30s` | S1 | La CTA grande entra per terza da destra; regolo in estensione |
| 04 | 1,65 | 41 | `scena_04_t1.65s` | S1 | Passaggio di luce sul titolo |
| 05 | 2,40 | 60 | `scena_05_t2.40s` | S1 | Fermo di lettura (senza due punti) |
| 06 | 2,78 | 70 | `scena_06_t2.78s` | T1 | Wipe di luce a metà; la CTA sta migrando verso la posizione media |
| 07 | 3,30 | 82 | `scena_07_t3.30s` | S2 | Hero card Sisal in arrivo, logo in dissolvenza; CTA media accanto |
| 08 | 4,20 | 105 | `scena_08_t4.20s` | S2 | Sisal · FINO A 5.200€ completo, riflesso vetro, indice 1/3 |
| 09 | 4,95 | 124 | `scena_09_t4.95s` | T2 | Wipe; CTA presente |
| 10 | 6,50 | 162 | `scena_10_t6.50s` | S3 | NetBet · FINO A 1.000€, indice 2/3 (stessa coreografia) |
| 11 | 7,10 | 178 | `scena_11_t7.10s` | T3 | Wipe |
| 12 | 8,60 | 215 | `scena_12_t8.60s` | S4 | William Hill · FINO A 255€, indice 3/3 (stessa coreografia) |
| 13 | 9,28 | 232 | `scena_13_t9.28s` | T4 | Wipe verso la comparazione; la CTA torna piccola |
| 14 | 10,10 | 252 | `scena_14_t10.10s` | S5 | Comparazione completa: tre card identiche, valori allineati |
| 15 | 11,00 | 275 | `scena_15_t11.00s` | S6 | Enfasi CTA: scala, anello, alone |
| 16 | 12,00 | 300 | `scena_16_t12.00s` | S6 | End frame stabile (fallback statico) |

## 4. Ambiente: campo di calcio visto dall'alto
- Sorgente: Higgsfield MCP, batch di 4 still 21:9 (nano_banana_pro → servito nano_banana_2, 2K), prompt "top-down aerial view of a generic empty football pitch at night" con esclusioni esplicite (persone, giocatori, pallone, bandierine, porte, spalti, folla, cartelloni, loghi, testi, numeri, architettura di stadio). Selezionata la variante **#21** (job `e190625a-b390-47f4-ba30-cc464acb0373`): ripresa perfettamente zenitale, cerchio di centrocampo al centro, linee sottili, nessun elemento IP. Le varianti #22 e #24 sono inclinate (non "dall'alto"), la #23 mostra l'intero campo piccolo con bordi neri: riserva. Dettagli in `07_asset_generati/README_higgsfield.md` §7.
- Trattamento nel template: ritaglio della fascia centrale (3168×927 da y=208) → 1018×298 (preview per lo storyboard; in produzione 2036×596); tinta nel verde Sisal (`mix-blend-mode: color` + screen leggero), luminosità +6 %, gradiente tonale alto/basso, ombra centrale morbida al 28 % e vignetta: il campo si legge, le linee restano sottili, i testi e le card stanno in primo piano.
- Camera per scena (scala / spostamento): S1 1,06 · S2 1,02 −28 px · S3 1,03 +22 px · S4 1,04 −12 px · S5 1,00; deriva 14 px sull'intera durata (ferma nella GIF).

## 5. Gerarchia di lettura e ruolo di Sisal
- S1: 1. "BONUS SPORT" 2. CTA. — S2–S4: 1. logo 2. valore 3. CTA. — S5/S6: 1. i tre valori 2. i tre loghi 3. CTA (in risalto) 4. titolo.
- Sisal: primo della sequenza (ordine richiesto, coincidente con il criterio decrescente), stessa inquadratura/durata degli altri; il lime del suo logo colora CTA e accenti tipografici, condivisi da tutto il banner. Nessun accento esclusivo sulla sua card in S5 (opzionale).

## 6. Transizioni (T1–T4)
Wipe di luce: la scena uscente viene mascherata da sinistra (`clip-path inset`), quella entrante rivelata da sinistra; sopra scorre una banda luminosa bianca-lime inclinata (larghezza 120 px, opacità a campana). Durata 0,30–0,35 s, easing in-out. Il cambio di camera avviene sotto la banda, così il taglio è percepito come uno stacco tra clip diverse. La CTA sta su un layer superiore, non mascherato: è continua e morfa tra le tre taglie durante T1 e T4.

## 7. Piano audio (richiesta del cliente; il brief originario "senza audio" è superato per MP4 master/web)

**Regole**: mai voiceover, mai voce sintetica, mai musica con voce, mai testo parlato o cantato. Nessun modello TTS/voce viene invocato. La traccia è composta da soli effetti e ambiente.

### 7.1 Verifica di ciò che Higgsfield MCP può fare per l'audio (2026-09-10)
`generate_audio`/`generate_audio_batch` sono strumenti **solo text-to-speech** (seed_audio, text2speech_v2, qwen_audio_tts): la descrizione ufficiale dello strumento dichiara che non può generare musica o sound effect per uso generale e che i modelli `mirelo_text_to_audio` (SFX) e `sonilo_music` esistono **solo per la pipeline di generazione giochi**. Quindi Higgsfield non viene usato per SFX/ambiente, e ovviamente non per voci. I modelli video con audio nativo produrrebbero picture+audio generativi non deterministici: esclusi.

### 7.2 Sorgente proposta: sintesi procedurale nel progetto (deterministica, senza diritti di terzi)
Script Python (numpy + ffmpeg, seme fisso) in `08_progetto/audio/`:

| Cue | t (s) | Descrizione | Livello indicativo |
|---|---|---|---|
| Bed "stadio lontano" | 0,00–12,00 | rumore rosa/marrone filtrato (200 Hz–3 kHz), modulazione lenta simile a un brusio di folla distante, leggero riverbero; fade-in 0,7 s (con l'ambiente), fade-out 0,6 s | ≈ −30 LUFS |
| Accensione | 0,10–1,60 | crescendo tenue (i riflettori si accendono) | −28 dBFS picco |
| Ingresso titolo | 0,25 · 0,45 | due soffi brevi e morbidi ("BONUS", "SPORT") | −22 dBFS picco |
| Ingresso CTA | 1,10 | soffio + tick leggero | −20 dBFS picco |
| Whoosh T1 | 2,55–3,00 | rumore bianco passa-banda con sweep 400 Hz → 4 kHz, inviluppo a campana, pan L→R (segue la banda di luce) | −14 dBFS picco |
| Whoosh T2 / T3 / T4 | 4,78–5,12 · 6,93–7,27 · 9,08–9,47 | identico a T1 (stesso campione) | idem |
| "Lock" valore | 4,10 · 6,25 · 8,40 | tick morbido quando le cifre si completano: **stesso suono, stesso livello per i tre operatori** | −18 dBFS picco |
| Card S5 | 9,50–10,20 | soffio unico per l'arrivo delle tre card | −20 dBFS picco |
| CTA S6 | 10,70 | "ping" corto (seno 880 Hz + armonica, decadimento 350 ms) + soffio dell'anello | −16 dBFS picco |

Mix: 48 kHz stereo; loudness integrata target **−20 LUFS**, true-peak ≤ −1 dBTP; nessun evento audio dopo 11,70 s. Consegna: AAC 128 kbps nel MP4 master/web; WAV 48 kHz 24 bit separato in `10_export/audio/`.

### 7.3 Alternativa
Libreria SFX licenziata fornita dal cliente: i file vengono montati nelle stesse posizioni e agli stessi livelli della tabella. Nessuna libreria non licenziata, nessun audio estratto da video di terzi.

### 7.4 Consegne audio/muto
`…_MASTER.mp4` e `…_WEB.mp4` con audio; `…_WEB_MUTO.mp4` senza traccia; GIF muta per natura. La comprensione del banner non dipende dall'audio.

## 8. Piano QC specifico per il concept M (in aggiunta a `11_qc/piano_qc.md`)
1. CTA presente e integra in **ogni** fotogramma da 1,10 s in poi, con posizione/taglia attese variabili nel tempo (grande → media → piccola → enfasi): il controllo campiona la pill nella posizione calcolata dalla stessa funzione del template.
2. Safe area piatta in tutti i 300 fotogrammi anche **durante i wipe** (nessuna banda di luce sotto y=210).
3. Pari trattamento sequenziale: per S2/S3/S4 gli istanti di inizio/fine di hero, logo, "FINO A", cifre complete e riflesso identici in tempo relativo (verifica sulle costanti + diff dei fotogrammi ai tempi omologhi: stessa luminanza media della card, stessa altezza del valore).
4. Loghi: nessuna deformazione (rapporto larghezza/altezza uguale al file ufficiale ±0,5 %), nessun patch dietro; posizione stabile nel fermo di ogni clip e in S5.
5. Valori: stringhe DOM esattamente "5.200€", "1.000€", "255€" e stessa dimensione font per i tre.
6. Ambiente: nessun elemento IP nel ritaglio usato (verifica visiva a 2×); linee del campo con contrasto contenuto (≤ 25 % rispetto al prato) sotto le zone di testo.
7. Audio: nessuna voce (analisi spettrale + ascolto), loudness −20 LUFS ±1, true-peak ≤ −1 dBTP, eventi ai tempi della tabella (±1 frame), fine audio ≤ 11,70 s; `…_WEB_MUTO.mp4` senza stream audio.
8. Pesi: web MP4 ≤ 3,5 MB con audio; GIF ≤ 3,5 MB (300 fotogrammi: ambiente fermo, palette per scena; se supera, 12,5 fps).

## 9. Ruolo di Higgsfield MCP nel concept M
- **Ambiente**: campo visto dall'alto, generato (batch di 4, 8 crediti) e selezionato; in produzione verrà trasferito a 2036×596. Il campo notturno in prospettiva del concept A resta disponibile.
- **Audio**: non utilizzabile per SFX/ambiente (§7.1); mai per voce.
- **Testi, loghi, importi, €, CTA, disclaimer**: mai generati (vincolo del brief).

## 10. Che cosa succede dopo l'approvazione
1. Conferma di: durata (12 o 13 s), accento S5 sì/no, sorgente audio (procedurale o libreria del cliente), bed stadio sì/no, variante di campo (#21 selezionata; #23 in riserva).
2. Produzione: trasferimento ambiente a 2×, render 2× dei 300 fotogrammi, sintesi e mix audio, encoding master/web/muto/GIF, QC automatico + visivo, report.
3. Consegna in `10_export/` con nomi `BonusSport_970x250_25fps_12s_M_*`; il concept A resta disponibile.
