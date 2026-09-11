# Piano di compressione — famiglia orizzontale

| Uscita | Codec / parametri | 300×250 · 336×280 | 1920×1080 | Note |
|---|---|---|---|---|
| MASTER (archivio) | H.264 High 4:4:4 CRF 12 + MOV PCM 24 bit | 2–5 MB | 40–80 MB | non per distribuzione |
| WEB.mp4 (≤ 3,5 MB) | H.264 High 4:2:0, CRF 17 → adattivo, `veryslow`, `+faststart`, AAC 128k | ≈ 0,3–0,5 MB | **CRF 22–24, o `-maxrate 2,4M -bufsize 4,8M`** per stare in 3,5 MB su 10 s (2,8 Mbit/s totali) | 1080p a 3,5 MB in 10 s è stretto: si valuta la resa a 100 % sul contact sheet decodificato; se insufficiente, si consegna anche un WEB_HQ.mp4 (≈ 6–8 MB) dichiarato fuori soglia |
| WEB_MUTO.mp4 | come WEB senza traccia audio | | | extra |
| CONTROL.gif (≤ 3,5 MB) | palettegen/paletteuse 256 colori, dither bayer 3 | 25 fps se ≤ 3,5 MB, altrimenti 12,5 → 10 | **960×540 a 10 fps** (una GIF 1920×1080 di 10 s non sta in 3,5 MB): dichiarata come GIF di controllo a metà risoluzione | fallback ulteriore: 8 fps |
| ENDFRAME PNG | ultimo fotogramma 1× | < 200 KB | ≈ 2 MB | fallback statico |

Ordine di riduzione se si supera la soglia: frame-rate → palette → (solo GIF 1920) risoluzione; per il WEB.mp4 1920 → CRF, mai la risoluzione.
