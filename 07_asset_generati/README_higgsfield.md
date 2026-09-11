# Higgsfield MCP — valutazione delle capacità e piano d'uso

Data valutazione: 2026-09-10. Account: piano "ultra", **2.849 crediti** disponibili a inizio sessione (`balance`). Crediti spesi in questa fase: **~6** (4 immagini esplorative).

## 1. Che cosa offre Higgsfield MCP (catalogo esplorato con `models_explore`)

| Famiglia | Modelli rilevanti per questo progetto | Note utili |
|---|---|---|
| Immagine text-to-image / edit | `nano_banana_pro` (servito come Nano Banana 2, 2K, 21:9), `nano_banana_2`, `seedream_v4_5` (fino a 4K/6K), `seedream_v5_pro`, `flux_2` (pro/flex/max), `gpt_image_2` / `gpt_image_2_5` (typography, background trasparente), `recraft_v4_1` (vector/utility, palette controllata), `kling_omni_image`, `soul_*` (persone: **non serve**) | 21:9 è il rapporto più largo disponibile; il 970×250 (3,88:1) va ritagliato dal 21:9 (2,33:1). |
| Immagine utility | `image_background_remover`, `outpaint` / `flux_2_pro_outpaint`, `topaz_image`, `bytedance_image_upscale` (2K/4K) | Outpaint utile per estendere un ambiente ai bordi; upscale non necessario (il banner è 970 px). |
| Video | `seedance_2_0` (4–15 s, fino a 4K, `generate_audio:false`), `seedance_2_5`, `kling3_0` (3–15 s, sound off), `minimax_h3` (2K), `wan3_0[_prime]`, `veo3_1`, `cinematic_studio_3_0`, `gemini_omni_flash_1_1`, `grok_video_v15`, `flux_3_video` | Tutti supportano start_image (image-to-video); nessuno garantisce assenza di flicker/shimmer su fondi con bokeh. |
| Video utility | `video_deflicker`, `topaz_video` / `bytedance_video_upscale`, `sam_3_video` (rimozione sfondo), `hf_mult_motion_control` (Genjutsu) | `video_deflicker` è interessante se si adotta una clip generativa. |
| 3D | `generate_3d`, Scene Builder 3D | Non necessario: nessun oggetto 3D previsto. |
| Sandbox | `sandbox_exec`: Linux con ffmpeg, ImageMagick, Pillow, Playwright+Chromium, font Montserrat, internet | Usata per la conversione/trasferimento degli asset (vedi §4). |
| Workflow | `brand-asset-creation`, `product-photoshoot`, `video-editing`, `ad-multiplier`, UGC, faceless… | Nessuno è pensato per un display banner comparativo; non adottati. |

## 2. Costi rilevati (preflight `get_cost:true`, nessun job avviato)

| Modello / configurazione | Crediti |
|---|---|
| `nano_banana_pro`, 21:9, 2K | 2 |
| `seedream_v4_5`, 21:9, high | 1 |
| `gpt_image_2`, 21:9, 2K, high | 6,5 |
| `gpt_image_2_5`, 21:9, 2K, high, trasparente | 5,5 |
| `flux_2` max, 16:9, 2K | 6 |
| `kling3_0` pro, 10 s, 16:9, sound off | 17,5 |
| `minimax_h3`, 10 s, 21:9, 2K | 20 |
| `veo3_1` preview, 8 s, high | 58 |
| `wan3_0_prime`, 10 s, 1080p, no audio | 60 |
| `seedance_2_0`, 10 s, 21:9, 1080p, no audio | 90 |
| `cinematic_studio_3_0`, 10 s, 21:9, 1080p | 100 |

## 3. Esplorazione eseguita (non definitiva, autorizzata dal brief per rappresentare lo storyboard)

Batch di 4 still 21:9 (`generate_image_batch`), prompt senza testi/loghi/persone/marchi:

| # | Modello (richiesto → servito) | Soggetto | Esito [OSS] | File |
|---|---|---|---|---|
| 1 | `nano_banana_pro` → `nano_banana_2` | campo generico notturno, riflettori in bokeh, banda alta scura | **Migliore**: pulito, senza rumore, area superiore libera per la grafica, linea di campo generica, nessun elemento IP | `expl_01_nanobanana2_pitch_preview776.jpg` |
| 2 | idem | atmosfera astratta con raggi di luce | Elegante, molto scuro; il fascio in alto a sinistra compete col titolo (nella variante B è specchiato a destra) | `expl_02_…abstract…jpg` |
| 3 | `seedream_v4_5` high | campo notturno | Più saturo e "stock", pali dei riflettori letterali, erba molto dettagliata (costosa in compressione) | `expl_03_…jpg` |
| 4 | `seedream_v4_5` high | arena astratta bagnata | Suggestivo ma affollato di punti luce e riflessi; spalti appena percepibili | `expl_04_…jpg` |

Nota: il catalogo espone `nano_banana_pro`, ma il job risulta eseguito da `nano_banana_2` (campo `model` del risultato). Documentato per trasparenza; il risultato è comunque quello valutato.

Le preview sono a 776 px (JPEG q72): servono allo storyboard. In produzione l'ambiente definitivo verrà rigenerato/ritrasferito a risoluzione piena.

## 4. Vincolo tecnico scoperto e risolto: trasferimento degli asset

Il CDN dei risultati Higgsfield (`*.cloudfront.net`) è **bloccato dal proxy di questa sessione** (403 di policy), mentre la **sandbox Higgsfield ha internet** e vede i risultati. Canale adottato, testato e verificato (md5 identico):
- **Higgsfield → progetto:** `sandbox_exec` scarica il risultato, lo ridimensiona/ritaglia al formato utile (es. 1010×290 per l'ambiente con margine di drift), lo codifica JPEG/PNG e lo stampa in base64 a blocchi da 16 KB; i blocchi vengono ricomposti localmente e verificati con md5. Costo: ~1 chiamata ogni 12 KB → un ambiente 1010×290 JPEG q92 (~120 KB) ≈ 10 chiamate. **Praticabile per still, non per clip video** (una clip 970×250 di 9 s ≈ 2–4 MB ≈ 250+ chiamate).
- **Progetto → Higgsfield:** il repository è pubblico su GitHub: `media_import_url` può importare qualsiasi file pushato (es. lo styleframe come `start_image` per un image-to-video, o i loghi per test di compositing nella sandbox).
- **Se si adotta una clip generativa:** il compositing può avvenire **dentro la sandbox Higgsfield** (Playwright + ffmpeg presenti) partendo dal progetto pubblico su GitHub; il master risultante è però scaricabile solo dall'utente dal widget Higgsfield (per il vincolo sopra) e andrà aggiunto al repo manualmente. Questa è l'unica parte del workflow che richiederebbe un passaggio manuale: la segnalo prima di sceglierla.

## 5. Ruolo previsto per Higgsfield MCP nel concept raccomandato (dopo approvazione)

| Fase | Strumento | Cosa genera | Cosa NON genera |
|---|---|---|---|
| P1 Ambiente | `generate_image_batch` con `nano_banana_2`/`nano_banana_pro` (2K, 21:9) ×4–6 varianti + eventuale `seedream_v4_5` come confronto; selezione; eventuale `flux_2_pro_outpaint` se serve estendere i bordi | 1 still ambiente definitivo (campo notturno generico, banda superiore scura) | testi, loghi, importi, simboli €, CTA, disclaimer, persone, squadre, stemmi, sponsor, stadi riconoscibili |
| P2 Test di motion (opzionale, decisione a valle del test) | `generate_video` image-to-video dallo still scelto: `kling3_0` pro 10 s (17,5 cr.) e `minimax_h3` 10 s (20 cr.) come test economici; `seedance_2_0` 1080p (90 cr.) solo se i test convincono | clip 10 s di deriva lentissima dell'ambiente (haze, bokeh), da valutare per flicker/shimmer con analisi frame-diff nella sandbox | idem |
| P3 Compositing | **locale** (Playwright + ffmpeg locali, già verificati): ambiente Higgsfield come layer di fondo; loghi ufficiali, testi, valori e CTA come DOM separati | master PNG sequence → MP4 master, MP4 distribuzione, GIF | — |
| P4 QC | eventualmente `video_deflicker` sulla sola clip d'ambiente se adottata | — | — |

**Decisione di default** (motivata in `05_concept/concept.md`): ambiente **still** generato da Higgsfield + **movimento programmato deterministico** nel compositor (deriva 10 px / 9 s, scala 1,035→1,0, passaggio di luce, riflesso CTA). Una clip generativa verrebbe adottata solo se il test P2 mostra assenza di flicker e un guadagno percepibile, e solo dietro accettazione del passaggio manuale descritto al §4. Budget stimato totale: **≤ 150 crediti** (≈ 5% del saldo).


---

## 6. PRODUZIONE (dopo approvazione del 2026-09-10)

### 6.1 Generazione ambiente definitivo
Batch `generate_image_batch` di 4 still 21:9 con prompt affinati (orizzonte al 65%, banda alta scura e pulita, luci solo ai bordi, centro quieto, esclusioni esplicite di persone/pali/tabelloni/loghi/testi/bandiere/palloni):

| # | Job | Modello richiesto → servito | Esito | Decisione |
|---|---|---|---|---|
| 11 | `b8ed1902-6fd2-4492-8741-78614a84faa4` | nano_banana_pro → nano_banana_2 (3168×1344) | banda alta pulita, cerchio di centrocampo, bokeh piccolo ai bordi, centro scuro | **SELEZIONATO** |
| 12 | `fec46426-d89b-489a-87ea-16d5d5d01769` | idem | come 11 con foschia bassa, più sfocato | riserva |
| 13 | `a57deef0-cef5-4ba0-b3ab-954205e83c80` | idem | molto scuro, linea in primo piano dominante | scartato |
| 14 | `cc81dc34-df81-4187-a49b-6b4f770ff581` | seedream_v4_5 (6048×2592) | pali dei riflettori, **pallone e bandierina d'angolo** presenti | **scartato (elementi vietati)** |

Preview a 776 px in `higgsfield_produzione/`. Crediti spesi in produzione: 7 (3×2 + 1).

### 6.2 Trasferimento
Nella sandbox Higgsfield: ritaglio a rapporto 1018:298 centrato al 60% dell'altezza (crop 3168×927 da y=343), Lanczos a **2036×596** (2× dell'area ambiente del template, per il render a 2×), JPEG q90 4:4:4 (113 068 byte), md5 `0929c68958b445d34f6a3798c875094e`; 10 blocchi base64 da 16 KB ricomposti localmente e verificati (md5 identico). File: `08_progetto/assets/env/env_A_pitch_FINAL_2036x596.jpg`.

### 6.3 Ciò che NON è stato generato con Higgsfield
Testi, loghi, importi, simbolo €, CTA, disclaimer: composti dal template. Nessuna clip video generativa: il movimento dell'ambiente è programmato (parallasse deterministica a 4 layer + particelle), per garantire assenza di flicker e piena compressibilità; la decisione è motivata in `05_concept/concept.md` e `11_qc/strategia_compressione.md`.


---

## 7. CONCEPT M — ambiente "campo di calcio visto dall'alto" (2026-09-10, storyboard v2)

Batch `generate_image_batch` di 4 still 21:9, `nano_banana_pro` (servito `nano_banana_2`, 3168×1344), prompt di campo generico notturno visto dall'alto con esclusioni esplicite (persone, giocatori, pallone, bandierine, porte, spalti, folla, cartelloni, loghi, testi, numeri, architettura di stadio). Costo: 8 crediti.

| # | Job | Soggetto | Esito | Decisione |
|---|---|---|---|---|
| 21 | `e190625a-b390-47f4-ba30-cc464acb0373` | zenitale, cerchio al centro, linea di metà campo verticale | pulito, linee sottili, luci ai bordi alto/basso (ritagliate), **nessun elemento IP** | **SELEZIONATO** |
| 22 | `79514b54-65b7-4eb6-9eb8-7f15647a3da5` | zenitale con cerchio decentrato | in realtà inclinata (prospettiva), non "dall'alto" | scartato |
| 23 | `7aaef159-1e57-4a77-b778-4992bfa31766` | alta angolazione, campo intero | campo intero con bordi neri, suggestivo ma il campo è piccolo nel 970×250 | riserva |
| 24 | `2523bb8a-5f99-4b86-add0-9e7270a05403` | zenitale bagnato con foschia | inclinata e molto nebbiosa | scartato |

Trasferimento (preview per lo storyboard): ritaglio fascia centrale 3168×927 (y=208), Lanczos a 1018×298, JPEG q86 4:4:4 (29 807 byte), md5 `40a0dc0c3c5b7c15bce12887d35e2b40`, 3 blocchi base64 ricomposti e verificati. File: `08_progetto/assets/env/env_M_pitch_topdown_PREVIEW_1018x298.jpg`. **Produzione (2026-09-10)**: stesso ritaglio trasferito a **2036×596** (JPEG q86 4:2:0, 146 342 byte), md5 `ea1d842587991411dbbb9bc7673308fa`, 13 blocchi base64 ricomposti e verificati → `08_progetto/assets/env/env_M_pitch_topdown_FINAL_2036x596.jpg` (default del template).

Audio: verificato che gli strumenti audio di Higgsfield MCP sono solo text-to-speech (vedi `06_storyboard/storyboard_M.md` §7.1): non usati.


---

## 8. REVISIONE 2 del concept M (2026-09-10): ambiente sonoro "stadio" da clip video con audio nativo

Richiesta del cliente: il bed sintetico continuo non suonava come uno stadio reale; suggerito di generare lo sfondo con Higgsfield "con principio già di audio". Poiché `generate_audio` è solo text-to-speech, ho usato **modelli video con audio nativo** e ne ho estratto la sola traccia audio (la parte visiva resta lo still zenitale già approvato, per assenza di flicker e piena compressibilità; la clip video resta disponibile nella libreria Higgsfield del cliente).

| # | Job | Modello | Durata | Costo | Analisi audio (sandbox: ffmpeg + faster-whisper) | Decisione |
|---|---|---|---|---|---|---|
| 32 | `9d228081-8a7f-4fb4-8448-ba79bd806993` | veo3_1 (start_image = still e190625a) | 8 s, 48 kHz stereo | 22 cr. | −33,8 LUFS; **nessun segmento di parlato** (whisper base, VAD: 0 segmenti); energia 300–2000 Hz (72 %) con ondeggiamenti lenti (variazione inviluppo 0,34): brusio di folla credibile | **SELEZIONATO** → `08_progetto/audio/ambience_stadio_higgsfield_veo_8s.m4a` (AAC 64 kbps, md5 `a53bcd4668d2ad2763731fc9bc8a3ef3`, 6 blocchi); in mix esteso a 12 s con loop e crossfade di 0,5 s |
| 31 | `4daed520-6208-4fc5-85d5-bad2549764bb` | seedance_2_0 21:9 720p, generate_audio (start_image = still e190625a) | 12 s, 32 kHz | 54 cr. | −41,8 LUFS; nessun parlato; energia concentrata 100–800 Hz, quasi nulla sopra 2 kHz (rombo sordo, poco "folla") | scartato (non trasferito) |

Prompt (entrambi): campo zenitale notturno, camera fissa; audio "realistic stadium ambience only: distant crowd murmur, soft continuous hum with occasional swells, a few far isolated shouts, wind; no music, no announcer, no commentary, no speech, no singing, no chants with words, no whistles". Preset "IN THE DARK" proposto dalla piattaforma e rifiutato (`declined_preset_id`).

Crediti spesi in questa revisione: 76. Totale progetto: ≈ 97.

## 9. FAMIGLIA VERTICALE 300×600 / 320×480 / 160×600 (2026-09-11, fase storyboard)

Nessun job avviato, **0 crediti**. Lo sfondo verticale è una ri-inquadratura dello stesso still approvato del master (job `e190625a-b390-47f4-ba30-cc464acb0373`): fascia centrale verticale 896×1344 (cerchio di centrocampo + linea di metà campo), ridimensionata a 800×1200 q76 nel sandbox e trasferita in 9 chunk base64 (md5 `d73f25578e8675d9c66088b4e88d4f3b`) → `08_progetto/assets/env/env_M_pitch_topdown_VERT_800x1200.jpg`. Valutazione asset per asset e opzioni per il render 2× in `adaptations/vertical_family/family_system/higgsfield_strategy.md`.
