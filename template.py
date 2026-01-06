import os
from pathlib import Path
'''
import pathlib importiert das ganze Modul.
    → Dann muss man pathlib.Path schreiben.
    from pathlib import Path importiert nur die Klasse Path direkt.
→ Dann kann man einfach Path schreiben.
'''
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
'''
 „richtet“ das Logging-System ein

level=logging.INFO
Das level legt fest, ab welcher Wichtigkeitsstufe Log-Nachrichten überhaupt ausgegeben werden.
Die üblichen Level (von niedrig nach hoch):
DEBUG – sehr detaillierte Infos, hauptsächlich für Entwickler
INFO – normale Laufzeitinfos („alles läuft wie erwartet“)
WARNING – etwas ist ungewöhnlich, aber das Programm läuft weiter
ERROR – ein Fehler ist aufgetreten, eine Aktion hat nicht funktioniert
CRITICAL – sehr schwerer Fehler, das Programm ist möglicherweise nicht mehr nutzbar

format='[%(asctime)s]: %(message)s:'
Mit format sagt man, wie jede Logzeile aussehen soll.

%(asctime)s: Zeitstempel, wann die Log-Nachricht erzeugt wurde.
Beispiel: [2026-01-06 17:05:12,345]

%(message)s: Die eigentliche Log-Nachricht, also das, was man z. B. mit logger.info("Text") übergibt.
'''

list_of_files = [

    "src/__init__.py",
    "src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials,ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath) #übersetzt in windows filepath 
    filedir, filename = os.path.split(filepath) # Directory: C:/Users/Desktop Filename: file.txt , os.path.split teilt path in dir und dateiname

    if filedir !="": 
        os.makedirs(filedir, exist_ok=True) # exist_ok verhindert das erneute erstellen eines ordners
        logging.info(f"Directory: {filedir} wurde für die Datei: {filename} erstellt")
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # exists gibt an ob dieser pfad bereits existiert, oder die datei im pfad ist leer (wird nicht erfüllt wenn datei inhalt hat)
        with open(filepath, "w") as f:# wenn datei existiert wird sie geleert, wenn nicht dann wird sie erstellt
            pass # mache nichts (datei wird leer gelassen)
            logging.info(f"Leere Datei: {filepath} wurde erstellt")
    else:
        logging.info(f"Die Datei {filename} existiert bereits")