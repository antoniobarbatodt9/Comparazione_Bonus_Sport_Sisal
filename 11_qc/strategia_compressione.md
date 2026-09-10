# Strategia di compressione (con misure reali sulla sequenza di prova)

**Test eseguito** (2026-09-10) sulla sequenza di prova dello storyboard (225 PNG 970×250, ambiente = preview esplorativa, animazione identica a quella proposta). **Non è il banner definitivo**: serve a dimensionare la strategia. File in `09_preview/test_pipeline_out/`.

| Uscita | Impostazioni | Peso misurato | Verso il limite 3,5 MB |
|---|---|---|---|
| Master MP4 | libx264, preset slow, CRF 14, yuv420p | **324 KB** (287 kb/s) | — (il master può superare; non serve) |
| Master archivio | libx264, CRF 12, yuv444p | 449 KB | — |
| Distribuzione MP4 | CRF 23 | 98 KB | 2,8% |
| GIF 25 fps, 256 col., ambiente in deriva | palettegen diff, sierra2_4a | 9,1 MB | ✗ |
| GIF 12,5 fps, 256 col., ambiente in deriva | idem | 5,1 MB | ✗ |
| GIF 12,5 fps, 128 col., bayer | — | 1,9 MB | ✓ ma dither visibile |
| **GIF 25 fps, 256 col., ambiente fermo** | `bgmode=still`, palettegen diff, sierra2_4a, diff_mode=rectangle | **1,7 MB** | **✓ 49%** |
| GIF 12,5 fps, 256 col., ambiente fermo | idem | 0,99 MB | ✓ 28% |
| GIF 12,5 fps, 256 col., ambiente fermo, senza dither | — | 0,72 MB | ✓ (banding possibile) |

## Conclusioni operative
1. **MP4**: il vincolo di 3,5 MB non è un fattore. Distribuzione a **CRF 16–18** (qualità quasi-master, stimati 150–250 KB) invece di comprimere per peso. Nessun compromesso sul concept.
2. **GIF**: il costo è tutto nella deriva continua dell'ambiente (ogni fotogramma cambia interamente). Soluzione già prevista dal progetto: **nella GIF l'ambiente resta fermo** (`bgmode=still`); tutto il resto (ingressi, rivelazione, accento, riflesso CTA) è identico. Risultato: **25 fps pieni a 1,7 MB**. Se il master definitivo (ambiente a risoluzione piena, più dettagliato) supera 3,5 MB a 25 fps, il fallback è 12,5 fps (≈1 MB) mantenendo 256 colori e dither sierra.
3. **Scelte di design che pagano in compressione** (già nel concept): fondo scuro e a basso dettaglio sotto i testi; card semitrasparenti ma senza gradienti animati; un solo evento di luce; fermo finale lungo (5,1→9,0 s) quasi gratuito per H.264 e GIF diff.
4. **Leggibilità dopo compressione**: verificata sull'end frame *decodificato* dall'MP4 web e dalla GIF (non sui PNG), a 1×. Valori a 29 px/800 e loghi bianchi su scuro sopravvivono senza problemi al 4:2:0 e alla palette a 256 colori (fondo verde quasi monocromo → palette abbondante per bianchi e lime).
5. **Conversione GIF**: palette **per-diff** (stats_mode=diff) e `diff_mode=rectangle` per aggiornare solo i rettangoli cambiati; ambiente fermo → fotogrammi di fermo ≈ 0 byte.
6. **Misure da ripetere** sul master definitivo e riportare in `11_qc/report_qc.md`.

## Comandi di riferimento (usati nel test)
```
ffmpeg -framerate 25 -i f%04d.png -c:v libx264 -preset slow -crf 14 -pix_fmt yuv420p -movflags +faststart MASTER.mp4
ffmpeg -framerate 25 -i f%04d.png -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -movflags +faststart WEB.mp4
ffmpeg -framerate 25 -i still/f%04d.png -vf "fps=25,split[a][b];[a]palettegen=max_colors=256:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle" CONTROL.gif
```
