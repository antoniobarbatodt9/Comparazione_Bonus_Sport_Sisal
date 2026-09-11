# Piano di compressione — famiglia verticale

Stessa catena del master (ffmpeg da `imageio_ffmpeg`), parametri adattati alle aree (300×600 = 180 kpx, 320×480 = 154 kpx, 160×600 = 96 kpx; il master 970×250 = 242 kpx).

| Uscita | Codec / parametri | Peso atteso | Note |
|---|---|---|---|
| MASTER (archivio) | H.264 High 4:4:4 (`-pix_fmt yuv444p -crf 12`) + copia MOV | 4–8 MB | non per distribuzione |
| WEB.mp4 (distribuzione ≤ 3,5 MB) | H.264 High 4:2:0, `-crf 20 -preset slow -profile:v high -movflags +faststart`, GOP 50, `-an` | 0,8–1,6 MB | senza audio (brief); se un ad server richiede traccia audio silente, aggiungere `anullsrc` in un secondo file |
| CONTROL.gif (≤ 3,5 MB) | palettegen/paletteuse (256 colori, dither bayer 3), 12,5 fps (125 f) per 300×600 e 320×480; 160×600 a 25 fps se ≤ 3,5 MB altrimenti 12,5 | 1,5–3,3 MB | i gradienti dello sfondo sono la voce di costo: eventuale `stats_mode=diff` |
| ENDFRAME PNG | ultimo fotogramma 1× | < 200 KB | fallback statico |

Verifiche post-encoding: Q1, Q7, Q8 del piano qualità; se la GIF supera 3,5 MB si riduce prima il frame-rate (12,5 → 10 fps), poi la palette (256 → 192), mai la risoluzione.
