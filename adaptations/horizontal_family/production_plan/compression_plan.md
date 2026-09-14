# Piano di compressione — famiglia orizzontale

| Uscita | Codec / parametri | 300×250 · 336×280 | 1920×1080 | Note |
|---|---|---|---|---|
| MASTER (archivio) | H.264 High 4:4:4 CRF 12 + MOV PCM 24 bit | 2–5 MB | 40–80 MB | non per distribuzione |
| WEB.mp4 (≤ 3,5 MB) | H.264 High 4:2:0, `veryslow`, `+faststart`, AAC 128k; rettangoli **CRF 12** (revisione nitidezza: 0,50 / 0,58 MB) | ≈ 0,5–0,6 MB | **CRF 22–24, o `-maxrate 2,4M -bufsize 4,8M`** per stare in 3,5 MB su 10 s (2,8 Mbit/s totali) | 1080p a 3,5 MB in 10 s è stretto: si valuta la resa a 100 % sul contact sheet decodificato; se insufficiente, si consegna anche un WEB_HQ.mp4 (≈ 6–8 MB) dichiarato fuori soglia |
| WEB_MUTO.mp4 | come WEB senza traccia audio | | | extra |
| CONTROL.gif (≤ 3,5 MB) | palettegen/paletteuse 256 colori, dither bayer 3 | 25 fps se ≤ 3,5 MB, altrimenti 12,5 → 10 | **960×540 a 10 fps** (una GIF 1920×1080 di 10 s non sta in 3,5 MB): dichiarata come GIF di controllo a metà risoluzione | fallback ulteriore: 8 fps |
| ENDFRAME PNG | ultimo fotogramma 1× | < 200 KB | ≈ 2 MB | fallback statico |

Ordine di riduzione se si supera la soglia: frame-rate → palette → (solo GIF 1920) risoluzione; per il WEB.mp4 1920 → CRF, mai la risoluzione.

## Revisione nitidezza rettangoli (2026-09-14)
Il cliente ha giudicato poco nitidi 300×250 e 336×280 aperti sul PC (il player li ingrandisce ≈ 3×). Aggiunte, entro 3,5 MB: WEB nativo a CRF 12; **varianti 2×** dagli stessi frame 2× (`_2x_600x500_*`, `_2x_672x560_*`: MASTER CRF 12, WEB CRF 12 = 1,94 / 2,46 MB, WEB_MUTO, ENDFRAME) e GIF ad alta densità (600×500 a 8 fps = 3,31 MB; 336×280 a 1,5× 504×420 12,5 fps = 3,08 MB perché 672×560 supera i 3,5 MB anche a 8 fps). Ordine di riduzione GIF 2×: frame-rate → scala 1,5×.
