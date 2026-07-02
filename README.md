# 🐱 CercaGatti

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)](https://opencv.org/)
[![Ultralytics](https://img.shields.io/badge/YOLO-v8-red)](https://github.com/ultralytics/ultralytics)

**CercaGatti** è un progetto software per un robot autonomo in grado di individuare un gatto tramite una telecamera, riconoscerlo utilizzando YOLO e decidere in quale direzione muoversi per inseguirlo.

> ⚠️ **Stato attuale:** Il progetto è nelle prime fasi di sviluppo. Il robot fisico non è ancora stato costruito; il software viene testato esclusivamente tramite webcam.

---

## 📋 Funzionalità

### ✅ Implementate

- **Acquisizione video** — Cattura di frame dalla webcam tramite OpenCV.
- **Configurazione della videocamera** — Impostazione di risoluzione e FPS.
- **Visualizzazione del flusso video** — Finestra live con `cv2.imshow()`.
- **Chiusura controllata** — Uscita dall'applicazione premendo il tasto `q` o cliccando la X della finestra.
- **Riconoscimento oggetti con YOLO** — Rilevamento di oggetti nei frame utilizzando YOLOv8.
- **Estrazione dei risultati** — Parsing delle detection YOLO in una struttura dati Python (lista di dizionari con bounding box, nome della classe e confidence).
- **Disegno dei bounding box** — Visualizzazione dei rettangoli e dei nomi delle classi direttamente sul frame.
- **Divisione dell'immagine in aree** — Linee di demarcazione al 40% e 60% della larghezza per suddividere il frame in sinistra, centro e destra (funzioni di test per cerchio e rettangolo).

### 🗺️ Roadmap (Pianificate)

- [ ] Filtraggio delle detection per rilevare esclusivamente gatti.
- [ ] Calcolo del centro del gatto rilevato.
- [ ] Decisione della direzione del robot in base all'area di appartenenza del gatto.
- [ ] Controllo dei motori per l'inseguimento.
- [ ] Tracking del gatto tra frame consecutivi.
- [ ] Gestione della perdita del bersaglio.
- [ ] Ottimizzazione delle prestazioni (FPS, riduzione latenza).
- [ ] Integrazione con l'hardware del robot.

---

## 🛠️ Tecnologie

| Tecnologia | Utilizzo |
| --- | --- |
| **Python 3.8+** | Linguaggio principale |
| **OpenCV** | Acquisizione video, elaborazione frame, disegno grafico |
| **Ultralytics YOLOv8** | Riconoscimento oggetti in tempo reale |
| **NumPy** | Gestione array e operazioni numeriche |
| **Supervision** | Utility per computer vision |
| **Git** | Controllo versione |

---

## 📦 Installazione

1. **Clona il repository**

   ```bash
   git clone https://github.com/alberellooo/CercaGatti.git
   cd CercaGatti
   ```

2. **Crea un ambiente virtuale**

   ```bash
   python -m venv venv
   ```

3. **Attiva l'ambiente virtuale**
   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **Linux/macOS:**

     ```bash
     source venv/bin/activate
     ```

4. **Installa le dipendenze**

   ```bash
   pip install -r requirements.txt
   ```

5. **Avvia il progetto**

   ```bash
   python show_result.py
   ```

   *(Premi `q` per uscire dalla finestra video)*

---

## 📁 Struttura del progetto

```text
CercaGatti/
├── camera.py          # Gestione della telecamera: inizializzazione,
│                      # lettura frame, disegno linee, output video e chiusura
├── yolo.py            # Inizializzazione del modello YOLO, rilevamento
│                      # oggetti e parsing dei risultati
├── show_result.py     # Visualizzazione dei risultati: disegno dei bounding
│                      # box e dei nomi delle classi sul frame
├── config.py          # Configurazione del progetto (in fase di sviluppo)
├── main.py            # Entry point principale (in fase di sviluppo)
├── requirements.txt   # Dipendenze del progetto
├── README.md          # Documentazione
└── .gitignore         # File ignorati da Git
```

### Ruolo dei moduli principali

- **`camera.py`** — Si occupa di tutto il flusso di acquisizione video: inizializza la webcam, legge i frame, ne ricava le dimensioni, disegna le linee di divisione dell'immagine, mostra il video a schermo e gestisce l'uscita dal programma.

- **`yolo.py`** — Carica il modello YOLOv8 pre-addestrato, esegue il rilevamento degli oggetti su un frame e restituisce i risultati in una struttura dati ordinata (lista di oggetti con posizione, nome e confidenza).

- **`show_result.py`** — Prende i risultati di YOLO e li visualizza graficamente sul frame disegnando rettangoli attorno agli oggetti rilevati e scrivendo il nome della classe.

- **`main.py`** — Destinato a diventare il punto di ingresso principale che coordinerà tutti i moduli (attualmente in fase di sviluppo).

---

## 🚦 Stato del progetto

Il progetto è in fase **alpha/sviluppo iniziale**. Al momento il software è in grado di:

- Acquisire video in tempo reale dalla webcam.
- Rilevare oggetti generici con YOLOv8.
- Mostrare i risultati graficamente.
- Suddividere l'immagine in aree per future decisioni direzionali.

Il passo successivo è filtrare le detection per riconoscere esclusivamente gatti e iniziare a implementare la logica decisionale per il movimento del robot.

---

## 🤝 Contributi

Questo è un progetto personale in fase di apprendimento e sviluppo. Suggerimenti, idee e feedback sono benvenuti!

---

## 📄 Licenza

Distribuito sotto licenza MIT. Vedi il file `LICENSE` per maggiori informazioni.
