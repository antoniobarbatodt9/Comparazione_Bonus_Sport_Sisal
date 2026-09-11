# Piano qualità — famiglia verticale

Controlli automatici (estensione di `11_qc/qc_check_M.py` alle tre size) sui fotogrammi **decodificati** dai file di consegna, non sui PNG sorgente:

| # | Controllo | Soglia | Metodo |
|---|---|---|---|
| Q1 | Fascia disclaimer piatta su 250/250 fotogrammi | deviazione ≤ 3/255 da `#061a12` (MP4) · esatta su PNG | scansione pixel della banda |
| Q2 | CTA presente e in quadro dal fotogramma 33 alla fine | bounding box lime nell'area attesa | finestra di ricerca per fase (S1/hero/S5) |
| Q3 | Rapporti loghi (misurati su 2×) | ± 4 % rispetto ai PNG ufficiali | template matching |
| Q4 | Testi non modificati | OCR opzionale + confronto con il DOM (testi separati) | |
| Q5 | Nessun pixel non-sfondo entro 4 px dai bordi laterali (160×600: pulse) | | |
| Q6 | Ultimo fotogramma = stato completo (titolo, tre card, CTA) | confronto con `storyboard/sb_*_08` | SSIM ≥ 0,98 |
| Q7 | Durata 10,00 s, 250 f, 25 fps, nessuna traccia audio | ffprobe | |
| Q8 | Pesi ≤ 3,5 MB (WEB.mp4, GIF) | | |
| Q9 | Leggibilità a 100 % del file decodificato (FINO A, importi, CTA) | ispezione visiva dei frame decodificati ai momenti K2/K4/K7/K8 | contact sheet |
| Q10 | Coerenza con il master | contact sheet master vs verticali sui file decodificati | |

Esito richiesto: tutti PASS; qualsiasi FAIL blocca la consegna della size.
