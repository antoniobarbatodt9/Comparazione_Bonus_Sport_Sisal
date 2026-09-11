# Piano di produzione — famiglia verticale (da avviare SOLO dopo approvazione esplicita degli storyboard)

## Ingressi bloccati
- Template: `adaptations/vertical_family/src/banner_vertical.html` (parametri size/t), renderer `src/render_vertical.mjs`.
- Sfondo: `08_progetto/assets/env/env_M_pitch_topdown_VERT_800x1200.jpg` (per il 2×: ritrasferimento a 896×1344 q84 dello stesso ritaglio del job `e190625a…`, 0 crediti).
- Loghi, font, token: gli stessi file del master (nessuna copia, riferimenti relativi).
- Durata 10,0 s · 25 fps · 250 fotogrammi · **senza audio**.

## Fasi
1. **Freeze** dei parametri `LAYOUTS` e della timeline (questa consegna) → tag di commit.
2. **Render 2×** per size: `node render_vertical.mjs --size <S> --fps 25 --duration 10 --scale 2 --out 09_preview/vertical/<S>_2x` (deviceScaleFactor 2 → 600×1200, 640×960, 320×1200).
3. **Downsample Lanczos** a 1× con ffmpeg (stesso comando del master) → sequenza PNG di controllo `09_preview/vertical/<S>_frames`.
4. **Encoding** (vedi compression_plan.md): master H.264 4:4:4 archivio, MP4 distribuzione ≤ 3,5 MB, GIF ≤ 3,5 MB, end-frame statico PNG (fallback).
5. **QC automatico** (quality_plan.md) + report `11_qc/report_qc_vertical.md` con contact sheet dei file decodificati.
6. Consegna in `10_export/vertical/BonusSport_<S>_25fps_10s_M_{MASTER.mp4, WEB.mp4, CONTROL.gif, ENDFRAME_fallback_statico.png}`.

## Ordine di lavorazione
300×600 → 320×480 → 160×600 (dal formato più vicino al master per proporzione di lettura a quello più critico), ciascuna con QC prima di passare alla successiva.

## Tempi stimati (macchina attuale)
Render 2× ≈ 4–6 min per size; encoding + QC ≈ 2 min per size. Totale ≈ 25 min.

## Ciò che non cambia in produzione
Nessuna modifica al 970×250; nessun nuovo asset Higgsfield; nessun testo aggiunto; fascia disclaimer vuota nei file consegnati.
