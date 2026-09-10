# FASE 2 — Brand identity Sisal: audit (PARZIALE) e blocco di accesso

## 1. Stato: BLOCCO DOCUMENTATO — il sito ufficiale non è raggiungibile da questo ambiente

| Tentativo | Data/ora (UTC) | Esito | Evidenza |
|---|---|---|---|
| `https://www.sisal.it/` via curl (proxy di sessione) | 2026-09-10 15:34:52 | **403 al CONNECT — "policy denial"** del proxy di uscita dell'organizzazione | `04_brand_identity/blocco_accesso.log` |
| `https://www.sisal.it/` via WebFetch | 2026-09-10 15:35 | `EGRESS_BLOCKED: Access to www.sisal.it is blocked by the network egress proxy` | idem |
| `https://www.sisal.com/` via WebFetch (riferimento corporate secondario) | 2026-09-10 15:35 | `EGRESS_BLOCKED` | idem |

Il blocco è una **regola di policy di rete dell'ambiente di esecuzione** (non un errore transitorio del sito): il proxy rifiuta la connessione prima che parta la richiesta HTTP. Non è aggirabile e, come da brief, **non è stato aggirato**:
- non ho usato siti affiliati, comparatori, portali bonus, blog o portfolio;
- non ho usato copie archiviate di terzi (Wayback e simili: anch'essi bloccati e comunque non "sito ufficiale");
- non ho inventato palette, font, componenti o motion language di Sisal.

### Conseguenza sul progetto
Il layer "brand" del concept (palette UI, tipografia, raggio dei componenti, stile CTA, eventuali microinterazioni) è **PROVVISORIO** ed è derivato **esclusivamente** dai file ufficiali forniti in `01_loghi/`. Tutto il resto del lavoro (struttura, comparazione, storyboard, timing, safe area, pipeline, piano Higgsfield) **non dipende** dal brand audit e può essere valutato subito. Il template `08_progetto/banner.html` tiene tutti i token di brand in variabili CSS (`:root`), quindi l'allineamento al brand reale è un'operazione di sostituzione valori, non di rifacimento.

### Che cosa chiedo al cliente per chiudere il brand audit (uno dei due)
1. **Accesso di rete a `www.sisal.it`** per questa sessione (sblocco del dominio nel proxy), oppure
2. **Materiali ufficiali**: screenshot della home e di una pagina "Scommesse/Bonus" a 1×, e se possibile: nome del font del sito (o un file CSS/brand book), i valori HEX dei colori UI (verde/lime/fondo/CTA), il raggio dei bottoni.

Fino ad allora la palette e il font qui sotto vanno letti come "coerenti con il logo ufficiale", **non** come "brand identity ufficiale".

---

## 2. Che cosa è OSSERVATO dagli asset ufficiali forniti (`01_loghi/`)

Misure eseguite sui file con script (PyMuPDF/Pillow/numpy), 2026-09-10.

### 2.1 Logo Sisal — `sisal.svg` (colori) e `Sisal_white_neg_LRES.png` (negativo)
| Elemento | Valore rilevato | Classe |
|---|---|---|
| viewBox SVG | 2290 × 756 (rapporto 3,03:1) | [OSS] |
| Fill wordmark "Sisal" e stella grande | `#00643a` (verde scuro) | [OSS] |
| Fill stella media | `#b9d531` (lime) | [OSS] |
| Fill stella piccola | `#e22118` (rosso) | [OSS] |
| Tratto di contorno tra le stelle | `#5d9d36` (verde medio, solo stroke tecnico) | [OSS] |
| PNG negativo | 2126 × 678 px, contenuto utile 1786 × 575 px (rapporto 3,106:1), densità d'inchiostro 0,354 | [OSS] |
| Forma del wordmark | minuscolo con terminazioni arrotondate, aste morbide, "S" maiuscola; carattere geometrico-umanista, **bold arrotondato** | [OSS] |
| Deduzione | L'esistenza di una versione "white neg" ufficiale indica uso previsto **su fondi scuri/colorati** (tipicamente il verde `#00643a`) | [DED] |

### 2.2 Logo NetBet — `netbet.svg`, `NetBet_PrimaryLogo_White.png`
| Elemento | Valore | Classe |
|---|---|---|
| viewBox | 91 × 16 (5,69:1) | [OSS] |
| Colori SVG | "Net" `#ffffff`, "Bet" `#EB2743` (rosso) | [OSS] |
| PNG white | 837 × 218, contenuto 761 × 138 (5,51:1), densità 0,705 (glifi molto pieni) | [OSS] |

### 2.3 Logo William Hill — `williamhill.svg`, `WilliamHill_white.png`
| Elemento | Valore | Classe |
|---|---|---|
| viewBox | 4872,2 × 1000 (4,87:1) | [OSS] |
| Colori SVG | "William" corsivo `#dec790` (oro, con gradiente `#BCA979→#FCE1A4`), "HILL" `#ffffff` | [OSS] |
| PNG white | 2172 × 724, contenuto 2014 × 417 (4,83:1), densità 0,379 | [OSS] |

### 2.4 Conseguenze progettuali [DED]
- Tutti e tre i loghi hanno **bianco strutturale** (Sisal negativo; "Net"; "HILL"): il banner deve avere **fondo scuro** dietro i loghi. La direzione "editoriale chiara" è scartata (styleframe `05_concept/styleframe/C_editoriale_chiaro_SCARTATA_*.png` lo dimostra: i loghi bianchi spariscono).
- Rapporti molto diversi (3,1 / 5,5 / 4,8): la normalizzazione va fatta per **peso ottico** (area d'inchiostro), non per larghezza o altezza. Valori scelti nel template: Sisal 118 px, NetBet 112 px, William Hill 138 px di larghezza; altezze risultanti 38 / 20 / 29 px; proporzioni originali intatte (solo `width`, `height:auto`).
- Nessun logo viene ricostruito, ricolorato o deformato: si usano i PNG bianchi ufficiali com'è. Nel master finale verranno rasterizzati dagli SVG alla dimensione esatta (per NetBet e William Hill le versioni colore contengono già il bianco; per Sisal si usa il PNG negativo ufficiale, ad alta risoluzione in ingresso).

---

## 3. Palette PROVVISORIA (derivata dal logo, non dal sito)

| Token | Valore | Origine | Uso nel banner |
|---|---|---|---|
| `--sisal-green` | `#00643a` | [OSS] logo | tinta dell'ambiente, testo CTA |
| `--sisal-lime` | `#b9d531` | [OSS] logo | seconda riga del titolo ("SPORT"), fondo CTA, accento bordo card Sisal |
| `--sisal-red` | `#e22118` | [OSS] logo | **non usato** (evita conflitto col rosso NetBet) [PRO] |
| `--ground-0` | `#061a12` | [PRO] verde scurito | fondo banner e fascia disclaimer |
| `--ground-1` | `#0b3324` | [PRO] | gradiente ambiente |
| testo | `#ffffff` / bianco 72% | [PRO] | valori / etichette |

Contrasto (WCAG, calcolato): bianco su `#061a12` ≈ 17:1; `#06301d` su lime `#b9d531` ≈ 8,9:1; lime su `#061a12` ≈ 10:1. Tutti ampiamente sopra 4,5:1.

**Da verificare col sito**: se Sisal usa in UI un verde/lime diversi dal logo, un fondo chiaro, o una CTA di forma diversa (es. raggio pieno vs 8 px), i token si aggiornano in `banner.html` `:root`.

---

## 4. Tipografia PROVVISORIA (font sostitutivo dichiarato)

- **Font ufficiale del sito: NON VERIFICATO** (sito non accessibile). Non dichiaro alcun font come "font Sisal".
- **Caratteristiche desiderate** (dedotte dal wordmark: geometrico, tondo, bold, contatore aperti) [DED].
- **Alternativa adottata, con licenza compatibile:** **Montserrat** (SIL Open Font License 1.1, scaricato da Google Fonts il 2026-09-10, pesi 500–800, file in `04_brand_identity/font_provvisorio/`) per titolo, valori e CTA; **Inter** (SIL OFL 1.1) per etichette piccole ("FINO A", criterio) per la migliore leggibilità sotto i 12 px. Manrope scaricato come seconda opzione, non usato.
- Motivo della scelta: Montserrat 800 in maiuscolo ha proporzioni larghe, cifre tabulari nitide e un carattere geometrico coerente con la rotondità del wordmark, senza imitarlo.
- **"BONUS SPORT" e "SCOPRI DI PIÙ" usano lo stesso font e peso** (Montserrat 800, maiuscolo), come richiesto dal brief.
- Se il font ufficiale risulterà disponibile e riutilizzabile, la sostituzione è un cambio di `@font-face` nel template.

---

## 5. Elementi di identità NON osservati (dichiarazione esplicita)

Non ho potuto osservare: CTA reali del sito, componenti, forme, proporzioni, spaziature, superfici, bordi, ombre, iconografia, impaginazione, microinterazioni, motion language, regole d'uso del logo, rapporto fondo/testo/CTA. Le scelte corrispondenti nel concept sono **[PRO]** e vanno validate.

## 6. Registro fonti di questa fase
Vedi `03_fonti/fonti.md` (righe F-04 … F-10).
