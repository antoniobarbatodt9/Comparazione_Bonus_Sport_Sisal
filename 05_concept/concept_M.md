# Concept M — "Montaggio a scene" (richiesta del cliente, 2026-09-10)

Stato: **approvato, prodotto e rivisto (revisione 2) il 2026-09-10** — vedi `06_storyboard/storyboard_M.md` §0-bis: niente effetto vetro, ambiente stadio reale da clip Higgsfield con audio nativo, solo pulse sulla CTA finale. (12 s, sfondo zenitale, audio SFX+bed, nessun accento S5, indici n/3 rimossi). Storyboard v2 (revisione del 2026-09-10 sulle note del cliente: niente due punti, ingresso BONUS → SPORT → CTA, etichetta piccola eliminata, CTA più grande nelle scene operatore, sfondo campo di calcio visto dall'alto). Nessun master prodotto per questo concept. Il concept A (pannello unico, 9 s) resta consegnato in `10_export/` e non viene toccato.

## 1. Che cosa ho capito della richiesta (riassunto per conferma)

| # | Richiesta | Come la traduco |
|---|---|---|
| 1 | Il banner non è più un pannello unico: è una **sequenza di scene diverse, montate come clip separate**, con **transizioni** tra una scena e l'altra | 5 inquadrature (S1…S5) + 4 transizioni (T1…T4) + un'enfasi finale (S6) dentro l'ultima inquadratura; ogni scena ha una sua "camera" (leggero cambio di scala/posizione dell'ambiente) così che il taglio si senta come un vero cambio di scena |
| 2 | **Prima scena**: solo "BONUS SPORT  SCOPRI DI PIÙ", che occupa/si allinea a tutto il 970×250, con entrata, transizione e motion graphics adeguati | S1: titolo a 56 px su una sola riga con la CTA grande (230×52) subito a destra, centrati sull'intero formato, **senza due punti**; ingresso nell'ordine **BONUS → SPORT → CTA**; tracking che si assesta, regolo lime, passaggio di luce; poi wipe di luce verso S2 |
| 3 | **Inserimento sequenziale degli operatori**: prima Sisal, poi NetBet, poi William Hill | S2, S3, S4: una "hero card" per volta (300×158, logo 1,45× più grande che nel concept A, valore a 38 px) con accanto la **CTA media** (210×54): card e CTA formano un gruppo centrato; nessuna etichetta piccola; stessa coreografia e stessa durata per i tre (1,85 s ciascuno), indice "1/3 · 2/3 · 3/3" |
| 4 | **Mettere in risalto la CTA "SCOPRI DI PIÙ"** | La CTA è protagonista in S1 (grande, 230×52), resta grande anche nelle scene operatore (media, 210×54, accanto alla card), torna piccola (150×44) solo nella comparazione dove lo spazio è condiviso con le tre card, e in S6 riceve un'enfasi dedicata (scala, anello, alone, riflesso) sul fermo finale |
| 5 | Le scene sono **tutte coerenti e consequenziali** | Un'unica narrazione: annuncio (S1) → i tre operatori uno alla volta (S2–S4) → tutti insieme a confronto (S5) → azione (S6). Stesso ambiente, stessa palette, stessa tipografia, stessi materiali delle card; ciascun operatore rientra in S5 con lo stesso logo e lo stesso valore appena visto |
| 6 | **La CTA deve sempre essere presente in ogni scena** | Un'unica CTA che, una volta entrata (1,10 s, terza dopo BONUS e SPORT come richiesto), non sparisce mai: morfa grande → media → piccola durante le transizioni senza mai uscire dal quadro. Verificato fotogramma per fotogramma dal QC |
| 7 | **Sound effect** sulle transizioni e **effetto stadio** (se mantengo il concept) o altro | Traccia audio con: bed ambientale "stadio lontano" a basso volume, whoosh su ogni transizione, tick/impatto morbido sui valori che si completano, "ping" sulla CTA finale. Dettagli e alternative in `06_storyboard/storyboard_M.md` §6 |
| 8 | **MAI voiceover** | Nessuna voce, né parlata né cantata, né sintetica. Nessun modello TTS viene invocato. Regola inserita nel piano QC (controllo spettrale della traccia: nessuna componente vocale) |
| 9 | Durata **entro 13 s**; se troppo complicato/veloce, **fino a un massimo di 12 s** | Ho letto le due indicazioni come: obiettivo ≤ 12 s, tolleranza fino a 13 s. Propongo **12,0 s = 300 fotogrammi a 25 fps**; se preferisce più respiro sui fermi (S1 e S5) posso allungare a 13,0 s senza cambiare la struttura. **Da confermare.** |

## 2. Struttura (12,0 s)

```
S1 2,60 s │T1│ S2 Sisal 1,85 s │T2│ S3 NetBet 1,85 s │T3│ S4 William Hill 1,85 s │T4│ S5 comparazione 2,55 s (S6 enfasi CTA negli ultimi 1,30 s)
0,00–2,60  0,35  2,95–4,80        0,30  5,10–6,95         0,30  7,25–9,10              0,35  9,45–12,00
```
Le quattro transizioni sono **wipe di luce** (una banda luminosa inclinata attraversa il formato da sinistra a destra e "trascina" la scena nuova). Sono brevi (0,30–0,35 s) e uguali tra loro: il ritmo resta leggibile e le transizioni non competono con i contenuti.

## 3. Pari dignità nel montaggio sequenziale

- Ogni operatore ha **la stessa inquadratura, la stessa card, la stessa dimensione del logo-box, la stessa dimensione del valore, la stessa coreografia e la stessa durata** (1,85 s). Nessun operatore è più veloce, più piccolo, più scuro o sfocato.
- L'**ordine** Sisal → NetBet → William Hill è quello richiesto dal cliente e coincide con l'ordine decrescente del criterio confrontato; è lo stesso ordine di S5. Non c'è riordino durante l'animazione.
- In S5 le tre card sono identiche (168×146, valori a 29 px, stessa baseline). Nessuna claim di "migliore in assoluto"; nessuna etichetta di criterio (rimossa su richiesta).
- Unico privilegio del cliente: la CTA e gli accenti del titolo usano il lime del logo Sisal; l'accento sul bordo della card Sisal del concept A **non** è previsto in S5 (opzionale, vedi §5).

## 4. Ambiente e motion graphics

- Ambiente: **nuovo still Higgsfield, campo di calcio visto dall'alto** (job `e190625a…`, preview `08_progetto/assets/env/env_M_pitch_topdown_PREVIEW_1018x298.jpg`; cerchio di centrocampo al centro, linee sottili, notturno, tinto nel verde Sisal e attenuato; nessun elemento IP), con parallasse programmata e una "camera" diversa per scena (S1 1,06 centrata · S2 1,02 spostata −28 px · S3 1,03 +22 px · S4 1,04 −12 px · S5 1,00). Nella GIF l'ambiente è fermo per il peso.
- Nessuna clip video generativa: il montaggio è composto in modo deterministico (Playwright + ffmpeg), quindi senza flicker e pienamente comprimibile. Rimane valida l'opzione, già documentata, di sostituire l'ambiente con una clip Higgsfield se il cliente lo chiedesse (con il passaggio manuale descritto in `07_asset_generati/README_higgsfield.md` §4).
- Higgsfield **non** genera testi, loghi, importi, simboli €, CTA o disclaimer (vincolo del brief); vedi §6 del storyboard per il ruolo nell'audio.

## 5. Scelte aperte (da decidere in approvazione)

1. **Durata**: 12,0 s (proposta) oppure 13,0 s (fermi più lunghi in S1 e S5).
2. **Variante di campo**: #21 (zenitale, selezionata) oppure #23 (campo intero con bordi neri, riserva); intensità del campo regolabile (ora attenuata, "non invasiva").
3. **Accento sul bordo della card Sisal in S5** (come nel concept A): non previsto; attivabile.
4. **Audio**: bed stadio + SFX (proposta) oppure solo SFX senza bed. Sorgente dei suoni: sintesi procedurale nel progetto (proposta, nessun diritto di terzi) oppure libreria licenziata fornita dal cliente.
5. **Versione muta**: consegno comunque un MP4 senza traccia audio per i circuiti display che non ammettono audio (la GIF è muta per natura).
