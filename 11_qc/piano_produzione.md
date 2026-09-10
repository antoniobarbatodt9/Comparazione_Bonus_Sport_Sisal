# Piano di produzione (da eseguire solo dopo approvazione esplicita di concept e storyboard)

## Pipeline scelta e perché

**Compositing: HTML/CSS/JS deterministico → Chromium headless (Playwright) fotogramma per fotogramma → ffmpeg.**
- Ogni fotogramma è calcolato da `t` (nessuna dipendenza dal tempo reale): render ripetibile, zero frame drop, zero flicker.
- Loghi, testi, valori e CTA sono nodi DOM separati e modificabili; i loghi restano file ufficiali non ricostruiti.
- Il layer ambiente è un'immagine (Higgsfield) sotto il DOM: nessun elemento informativo è dentro l'asset generato.
- Tutta la toolchain è già presente e verificata in questo ambiente (Chromium 1194, ffmpeg 7.0.2 con libx264/gif/vp9, Pillow). Alternativa considerata e scartata: compositing nella sandbox Higgsfield (stessi strumenti) — necessaria solo se si adotta una clip video generativa, con passaggio manuale di download.

## Fasi

| # | Fase | Strumenti | Output | Stima |
|---|---|---|---|---|
| 0 | Recepimento approvazione + eventuali note (durata, ordine card, alone, font/palette ufficiali se forniti) | — | `08_progetto/config.json` aggiornato | — |
| 1 | Ambiente definitivo: batch 4–6 still (`nano_banana_2`/`pro` 2K 21:9, 1–2 varianti `seedream_v4_5`), prompt affinati sulla base della #1 esplorativa (più buio in alto, punti luce fuori dall'area card, erba meno dettagliata) | Higgsfield `generate_image_batch`, `jobs_wait` | 1 still selezionato | ~10–15 crediti |
| 2 | Trasferimento: nella sandbox Higgsfield ritaglio a 1010×290 (area con margine di drift), Lanczos, leggero darkening/blur programmato; trasferimento a blocchi e verifica md5 | `sandbox_exec` | `08_progetto/assets/env/env_A_pitch_FINAL.jpg` (q92) | ~10 chiamate |
| 3 | (Opzionale, decisione a valle) Test image-to-video: `kling3_0` pro 10 s e `minimax_h3` 10 s dallo still; analisi frame-diff/flicker nella sandbox; adozione solo se stabile e migliore della deriva programmata e con accettazione del download manuale | Higgsfield `generate_video_batch`, `sandbox_exec` (ffmpeg) | report + decisione | ~40 crediti |
| 4 | Render master: 225 PNG a 2× (1940×500, deviceScaleFactor 2) → downsample Lanczos a 970×250 (bordi loghi/testi più nitidi) | `render.mjs --scale 2`, Pillow | `09_preview/master_frames/` | ~4 min |
| 5 | Encoding master MP4 (CRF 12, preset slow, yuv420p, +faststart; copia yuv444p per archivio) | ffmpeg | `10_export/BonusSport_970x250_25fps_9s_MASTER.mp4` | 1 min |
| 6 | Versione di distribuzione ≤ 3,5 MB (CRF 16–18 two-pass o CRF single; il test dà 0,1–0,45 MB: ampio margine, quindi si privilegia la qualità) | ffmpeg | `10_export/BonusSport_970x250_25fps_9s_WEB.mp4` | 1 min |
| 7 | GIF di controllo ≤ 3,5 MB: render dedicato con `bgmode=still` (ambiente fermo), 25 fps se ≤ 3,5 MB (test: 1,7 MB) altrimenti 12,5 fps; palette 256 diff-based, dither sierra2_4a, `diff_mode=rectangle` | ffmpeg | `10_export/BonusSport_970x250_CONTROL.gif` | 2 min |
| 8 | QC (vedi `piano_qc.md`) e report con misure | script + ispezione visiva | `11_qc/report_qc.md` | 30 min |
| 9 | Consegna: commit/push di progetto, asset, export e report | git | branch `claude/intelligent-feynman-sqxtf5` | — |

Tempo totale stimato dopo l'approvazione: **circa 2–3 ore** di lavoro effettivo (incluse attese Higgsfield), esclusa l'eventuale fase 3.

## Cosa NON viene fatto senza ulteriore richiesta
- Altre size (728×90, 300×250 ecc.): la struttura è predisposta, ma non richiesta ora.
- Disclaimer, logo ADM, 18+: mai inseriti; la safe area resta vuota.
- Audio: nessuno.
- Loop dedicato: non previsto (riproduzione singola con end frame stabile).
