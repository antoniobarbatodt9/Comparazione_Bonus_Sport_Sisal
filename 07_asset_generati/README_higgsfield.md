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
