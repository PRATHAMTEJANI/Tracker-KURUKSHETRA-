# Tracker-KURUKSHETRA-

# 🧠⚔️ KURUKSHETRA AI

### The Battle Between Focus & Distraction

> **Kurukshetra AI** is an offline, behavior-based cognitive drift tracker that detects whether you are truly focused or just appearing productive.

This project does **not** track tasks.  
It tracks **human behavior**.

---

## 🚀 Why Kurukshetra AI?

Most productivity tools ask:

> _“What task are you working on?”_

Kurukshetra AI asks:

> **“Are you actually mentally present?”**

It identifies the **gap between intention and behavior** using real-time signals like mouse movement, keyboard activity, and app usage.

---

## 🧠 What It Does

✔ Tracks **mouse movement & keyboard activity** (behavior only, no content)  
✔ Detects **active applications** and **time spent on each app**  
✔ Analyzes patterns every **1 minute**  
✔ Classifies sessions into:

- **Focused Work**
- **Fake Productivity**
- **Mind Drift**

✔ Warns you when unnecessary activity continues  
✔ Works **100% offline**  
✔ Stores data locally in JSON  
✔ Visualizes insights using an **Electron dashboard**

---

## 📊 Dashboard Features (Electron)

- 📈 Focus score timeline
- 📊 App-wise usage graphs
- 📄 Full session data shown directly in UI (JSON viewer)
- ⚡ Fast understanding without opening raw files

---

## 🛠️ Tech Stack

### Core Logic

- **Python**
- `pynput` – mouse & keyboard behavior
- `psutil` – system & app tracking
- `ctypes` – Windows active app detection
- `plyer` – system notifications

### Visualization

- **Electron.js**
- **Chart.js**
- HTML / CSS / JavaScript

---

## 🔒 Privacy First

- ❌ No cloud
- ❌ No keystroke content logging
- ❌ No screenshots
- ✅ Only behavioral metadata
- ✅ Fully offline & local

Kurukshetra AI is designed to be **honest, not invasive**.

---

## 🏗️ Project Structure

Tracker-KURUKSHETRA-/
│
├── main.py # Core tracker
├── analyzer.py # Focus & drift logic
├── storage.py # Local JSON storage
├── ui.py # Console summary
│
├── data/
│ └── sessions.json # Session data
│
├── dashboard/ # Electron dashboard
│ ├── index.html
│ ├── renderer.js
│ ├── main.js
│ ├── style.css
│ └── package.json
│
└── README.md

---

## ▶️ How to Run

### 1️⃣ Python Tracker

```bash
pip install pynput psutil plyer
python main.py

2️⃣ Electron Dashboard
cd dashboard
npm install
npm start

🧪 Example Output
[2025-01-01 19:31] Fake Productivity | Score: 42
App usage: chrome.exe (40s), code.exe (20s)
⚠️ Warning: Unnecessary activity detected

🧠 Is This AI?

Yes — Kurukshetra AI is a behavioral intelligence system.

It:

Perceives user behavior

Reasons using heuristics

Acts through insights & warnings

This is rule-based / heuristic AI, the foundation of many real-world intelligent systems.

🔮 Future Scope

User-specific learning & baselines

Heatmaps (hour × focus)

App-specific drift detection

ML-based behavior clustering

System tray background mode

🏁 Final Thought

Kurukshetra AI isn’t a productivity app.
It’s a mirror.

It shows whether you are truly focused —
or just fighting the battle in your own mind.

👨‍💻 Built by Arjun

Build in public. Think deeply. Stay honest.


---

## 🔥 NEXT (Optional)
Agar bole to main:
- ⭐ GitHub badges add kar dunga
- 📸 Screenshot section bana dunga
- 🧑‍💼 Resume-ready project summary likh dunga
- 🎯 Hackathon pitch version bana dunga

Bas bol bhai 😎
```
