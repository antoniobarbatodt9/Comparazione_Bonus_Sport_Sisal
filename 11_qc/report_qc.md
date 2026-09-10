# Report QC — Bonus Sport 970×250 (produzione 2026-09-10)

Sorgenti: `09_preview/master_frames/` (225 PNG 970×250 da render 2× + Lanczos), export in `10_export/`.
Ambiente: Higgsfield job `b8ed1902…` (nano_banana_2), trasferito e verificato (md5).

## Pesi export
| File | Byte | MB |
|---|---|---|
| BonusSport_970x250_25fps_9s_MASTER.mp4 | 549702 | 0.55 |
| BonusSport_970x250_25fps_9s_MASTER_444_archivio.mp4 | 758359 | 0.76 |
| BonusSport_970x250_25fps_9s_WEB.mp4 | 235220 | 0.24 |
| BonusSport_970x250_CONTROL.gif | 2097774 | 2.10 |


## Controlli automatici (qc_check.py)

- ✅ Fotogrammi: 225 (atteso 225) · dimensione (970, 250) (atteso (970, 250))
- ✅ CTA visibile in ogni fotogramma (lime + testo scuro): tutti
- ✅ Safe area 0,210 970×40 piatta e vuota in ogni fotogramma: tutti
- ✅ Stabilità zona card nel fermo (max diff medio/frame): 0.087/255 (soglia 0,6; CTA riflesso escluso)
- ✅ Loghi stabili dopo 2,0 s fuori dalle finestre di effetto (riflesso vetro f76–f95, accento f100–f154): max diff medio/frame 0.048/255 al frame 220 (soglia 0,8)
- ✅ Posizione di ogni logo invariata tra f60 e f224 (baricentro pixel chiari nel box logo): Sisal Δ=(0.07,0.04) · NetBet Δ=(0.00,0.00) · William Hill Δ=(0.00,0.00) px (soglia 0,25)
- ✅ Master MP4: 0.55 MB · Duration: 00:00:09.00, start: 0.000000, bitrate: 488 kb/s · Stream #0:0[0x1](und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(progressive), 970x250, 485 kb/s, 25 fps
- ✅ Web MP4: 0.24 MB (limite 3,5 MB) · Duration: 00:00:09.00, start: 0.000000, bitrate: 209 kb/s · Stream #0:0[0x1](und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(progressive), 970x250, 206 kb/s, 25 fps
- ✅ GIF di controllo: 2.10 MB (limite 3,5 MB) · Duration: 00:00:09.00, start: 0.000000, bitrate: 1864 kb/s · Stream #0:0: Video: gif, bgra, 970x250, 25 fps, 25 tbr, 100 tbn
- ✅ End frame decodificato (web): luminanza media fascia valori 156 vs fondo card 56 (fascia valori deve superare il fondo di ≥ 40)
- ✅ End frame decodificato (gif): luminanza media fascia valori 157 vs fondo card 56 (fascia valori deve superare il fondo di ≥ 40)

- **ESITO COMPLESSIVO: TUTTI I CONTROLLI AUTOMATICI SUPERATI**

## Controlli visivi (ispezione a 1× e 2×)
- Fotogrammi master a 2× (`09_preview/master_frames_2x`, f0035 e f0224 ispezionati): ambiente integrato sotto i dati, banda alta pulita, cerchio di centrocampo sotto le card, loghi ufficiali nitidi e non deformati, nessuna maschera o rettangolo dietro i loghi.
- End frame decodificati dagli export (`endframe_decodificato_WEB.png`, `endframe_decodificato_GIF.png`): valori "5.200€ · 1.000€ · 255€" leggibili e uguali per dimensione; bordo lime su Sisal sottile e pulito; CTA integra; GIF senza dithering visibile sui testi (palette diff a 256 colori con fondo quasi monocromo).
- Storyboard v2 (`06_storyboard/storyboard_v2_contact_sheet.png`): ingressi simultanei delle card e dei loghi verificati sui fotogrammi f27/f40; rivelazione dei valori completa a f69; unico accento a f110; nessun riordino; safe area sempre vuota.
- Pari dignità: card 168×146 identiche; valori 29 px identici; loghi normalizzati per peso ottico (118/112/138 px) senza deformazioni; nessun competitor sfocato/ridotto.
- Loghi: NetBet e William Hill con baricentro identico tra f60 e f224 (Δ = 0,00 px); Sisal Δ = 0,07 px dovuto ai pixel di antialias resi più chiari dall'alone (nessuno spostamento reale).

## Checklist di conformità al brief
| Requisito | Esito |
|---|---|
| 970×250, 25 fps, 8–10 s (9,00 s), senza audio | ✅ (ffprobe: 970x250, 25 fps, 00:00:09.00, nessuna traccia audio) |
| Titolo "BONUS SPORT", loghi Sisal/NetBet/William Hill, valori "FINO A 5.200€ / 1.000€ / 255€", CTA "SCOPRI DI PIÙ" | ✅ testuali, non arrotondati, dal `config.json` |
| CTA visibile in tutta la durata | ✅ 225/225 fotogrammi |
| Safe area disclaimer libera per tutta la durata | ✅ 970×40 px in y 210–250, piatta `#061a12`, dev. std 0 in 225/225 fotogrammi |
| Nessun claim "migliore in assoluto" | ✅ nessun testo oltre gli obbligatori |
| Card Sisal non più grande, valore non più grande, competitor non penalizzati | ✅ misure identiche; accento solo su bordo/luce |
| Loghi non ricostruiti, proporzioni intatte, nessuna toppa | ✅ file ufficiali, `height:auto` |
| Contesto sportivo generico senza IP | ✅ ambiente Higgsfield selezionato senza pallone/bandierine/persone/stemmi (variante con pallone scartata) |
| Nessun testo/logo/importo/€/CTA generato da Higgsfield | ✅ solo l'ambiente è generato |
| Master MP4 alta qualità · web ≤ 3,5 MB · GIF ≤ 3,5 MB | ✅ 0,55 MB · 0,24 MB · 2,10 MB |
| Nessun disclaimer/simbolo regolamentare inserito | ✅ |
| Nessuna size aggiuntiva | ✅ non richiesta |

Riproducibilità: `bash 08_progetto/make_master.sh assets/env/env_A_pitch_FINAL_2036x596.jpg 9 25` rigenera fotogrammi ed export; `python3 11_qc/qc_check.py …` rigenera i controlli automatici.
