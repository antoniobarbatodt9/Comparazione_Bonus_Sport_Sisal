# Piano qualità — famiglia orizzontale

Controlli automatici sui fotogrammi **decodificati** dai file di consegna (estensione di `11_qc/qc_check_vertical.py`):

| # | Controllo | Soglia | Metodo |
|---|---|---|---|
| Q1 | Fascia disclaimer piatta su 250/250 fotogrammi | dev. ≤ 3/255 (MP4) · esatta (PNG) | scansione della banda |
| Q2 | CTA presente dal fotogramma 33 alla fine, nella finestra attesa per fase | bounding box lime | finestre S1 / hero / S5 per size |
| Q3 | Loghi: rapporto box DOM = rapporto file (tol. 0,5 %) e inchiostro vs PNG ufficiale (tol. 5 %) | | come QC verticale |
| Q4 | Testi non modificati | confronto con il DOM | |
| Q5 | Nessun pixel non-sfondo entro 4 px dai bordi laterali | | |
| Q6 | Ultimo fotogramma = stato completo | SSIM ≥ 0,98 vs `storyboard/sb_*_08` | |
| Q7 | Durata 10,00 s (o 12,00 per il 1920 se scelto), 25 fps, traccia audio presente su MASTER/WEB, assente su MUTO/GIF; −20 LUFS ± 1, TP ≤ −1 dBTP, ultimo evento ≤ 9,95 s | ffprobe / ebur128 | |
| Q8 | Pesi ≤ 3,5 MB (WEB.mp4, GIF) | | 1920: vedi compression_plan |
| Q9 | Leggibilità a 100 % dei file decodificati (FINO A, importi, CTA) ai momenti K2/K4/K7/K8 | ispezione | contact sheet |
| Q10 | Coerenza con il master sui file decodificati | contact sheet | |

Esito richiesto: tutti PASS; un FAIL blocca la consegna della size.
