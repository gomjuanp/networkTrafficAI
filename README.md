# 🛡️ Network Traffic AI Detector

A work-in-progress Python tool designed to **capture network traffic**, analyze it using **Wireshark (TShark)**, and apply **AI models** to detect potential cyberattacks.

---

## 🚀 Project Overview

- **Live traffic capture** via TShark  
- **Feature extraction** using `pyshark`, `pandas`, `scikit-learn`  
- **Machine learning model** (e.g. Random Forest) for detecting anomalies/attacks  
- Intended for use in a **safe, isolated test environment**

---

## 🧪 Current Status

This project is in **active development**.  
✅ Core pipeline is in place (capture → parse → model inference).  
⚠️ I am still exploring:
- Methods to **collect and label own datasets safely**
- Best practices for **testing detection** in controlled environments

---

## 🔧 Install & Run

```bash
# Install dependencies
pip install pyshark pandas scikit-learn

# Capture packets for 10 seconds and parse into CSV
python capture_and_parse.py

# Train or load the ML model
python train_model.py

# Run live detection
python detect_live.py --interface eth0
