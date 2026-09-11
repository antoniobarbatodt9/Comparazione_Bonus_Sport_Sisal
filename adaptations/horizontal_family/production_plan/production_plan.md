# Piano di produzione — famiglia orizzontale (da eseguire solo dopo approvazione degli storyboard)

## Ingressi bloccati
- Template `adaptations/horizontal_family/src/banner_horizontal.html` + `src/render_horizontal.mjs` (parametri `LAYOUTS`, timeline).
- Sfondo `08_progetto/assets/env/env_M_pitch_topdown_169_1920x1080.jpg` (1920 a 2×: ritrasferimento del ritaglio 2389×1344 nativo, 0 crediti, oppure render 1× diretto — da decidere con il gate).
- Loghi, font, token: file del master (riferimenti relativi).
- Durata 10,0 s · 25 fps · 250 fotogrammi · **con audio** (profilo `horizontal` = `vertical` + pan L→R sui whoosh); 1920×1080 eventualmente a 12 s con profilo `master`.

## Fasi
1. Freeze dei parametri → commit.
2. Render 2× per size (`--scale 2`, drift + still per la GIF) → `09_preview/horizontal/<S>_2x` (1920: 3840×2160, ≈ 25–35 min).
3. Downsample Lanczos → `09_preview/horizontal/<S>_frames`.
4. Audio: `make_audio.py --profile horizontal` → `08_progetto/audio/BonusSport_H_audio_48k.wav`.
5. Encoding (compression_plan.md): MASTER.mp4 4:4:4 CRF 12, archivio MOV PCM, WEB.mp4 ≤ 3,5 MB AAC 128k, WEB_MUTO.mp4, CONTROL.gif ≤ 3,5 MB, ENDFRAME PNG.
6. QC (`11_qc/qc_check_horizontal.py`, estensione dello script verticale) + report `11_qc/report_qc_horizontal.md` + contact sheet dei frame decodificati.
7. Consegna in `10_export/horizontal/BonusSport_<S>_25fps_10s_M_*`.

## Ordine
300×250 → 336×280 → 1920×1080 (il 16:9 per ultimo: render più lungo e scelta 10/12 s).

## Tempi stimati
Rettangoli: render 2× ≈ 3 min ciascuno + encoding/QC 2 min. 1920×1080: render 2× ≈ 30 min (o 1× ≈ 8 min), encoding ≈ 5 min. Totale ≈ 50 min.
