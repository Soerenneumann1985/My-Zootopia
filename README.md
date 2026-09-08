# Animals Web Generator

Dieses Projekt generiert eine einfache Webseite (`animals.html`), die Tierdaten aus einer externen Quelle lädt und darstellt.  
Die Daten werden über ein Python-Skript abgerufen und anschließend in eine HTML-Datei geschrieben.

## 📁 Projektstruktur

- `AnimalsWebGenerator.py` – Hauptskript zum Abrufen und Generieren der HTML-Datei  
- `animals.html` – Ausgabedatei, die automatisch erstellt wird  
- `.env` – enthält API-Keys oder Konfigurationswerte  
- `requirements.txt` – listet alle benötigten Python-Abhängigkeiten  
- `.venv/` – virtuelle Umgebung (nicht im Repo benötigt)

## 🚀 Installation

1. Virtuelle Umgebung erstellen:
   ```bash
   python -m venv .venv
2. Virtuelle Umgebung aktivieren:

**Windows**
.\venv\Scripts\activate

**Linux / macOS**
source .venv/bin/activate



3. Abhängigkeiten installieren:
   
pip install -r requirements.txt


---

## ▶️ Nutzung

Starte das Skript:
python AnimalsWebGenerator.py


Danach findest du die generierte Datei **animals.html** im Projektordner.

---

## 🔐 Umgebungsvariablen (.env)

Die Datei `.env` enthält Konfigurationswerte wie API-Keys oder URLs.

Beispiel:
API_KEY=dein_api_key


---

## 📦 Abhängigkeiten

Die wichtigsten Pakete:

- **[requests](ca://s?q=Erklaere_requests)** – zum Abrufen von Daten aus dem Internet  
- **[python-dotenv](ca://s?q=Erklaere_python_dotenv)** – zum Laden der `.env`‑Datei

---

## 📜 Lizenz

Dieses Projekt ist privat und dient zu Lernzwecken.






