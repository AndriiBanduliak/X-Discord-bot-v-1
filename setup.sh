#!/bin/bash

echo "📌 Erstelle und aktiviere eine virtuelle Umgebung..."
python3 -m venv venv
source venv/bin/activate

echo "📌 Installiere erforderliche Pakete..."
pip install -r requirements.txt

echo "✅ Setup abgeschlossen! Starte den Bot mit: source venv/bin/activate && python bot.py"
