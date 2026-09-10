Test di pipeline (NON definitivi). Servono a verificare toolchain e pesi di compressione con la sequenza dello storyboard (ambiente = preview esplorativa a bassa risoluzione).
- test_pipeline_out/TEST_master_crf14.mp4 — 324 KB, 970×250, 25 fps, 9,00 s
- test_pipeline_out/TEST_dist_crf23.mp4 — 98 KB
- test_pipeline_out/TEST_master_crf12_444.mp4 — 449 KB (yuv444p)
- test_pipeline_out/TEST_gif_25fps_256c_STILLBG.gif — 1,7 MB (ambiente fermo)
- test_pipeline_out/TEST_gif_12fps_256c_STILLBG.gif — 0,99 MB
- test_pipeline_out/TEST_gif_12fps_256c_STILLBG_nodither.gif — 0,72 MB
- test_pipeline_out/TEST_gif_12fps_128c_bayer.gif — 1,9 MB (ambiente in deriva, 128 colori)
Le GIF con ambiente in deriva a 256 colori (5,1 MB e 9,1 MB) non sono versionate: vedi 11_qc/strategia_compressione.md.
- test_template/ — primi 5 fotogrammi di verifica del template con guide di layout.

## Produzione (2026-09-10)
Le sequenze di fotogrammi del master (`master_frames_2x/`, `master_frames/`, `gif_frames_2x/`, `gif_frames/`) non sono versionate perché rigenerabili in modo deterministico con `08_progetto/make_master.sh`. Log della pipeline: `make_master.log`.
