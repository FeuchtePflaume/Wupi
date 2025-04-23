Wasseruhr-Überwachungssystem

Ein Überwachungssystem für Wasseruhren, das Bilder vom Zählerstand aufnimmt, verarbeitet und speichert.


Funktionen

* Bilder vom Zählerstand aufnehmen und verarbeiten
* Texterkennung und Zeigererkennung durchführen
* Daten speichern und anzeigen
* Automatisches Bildmachen am 1. Tag im Monat um 4 Uhr
* Manuelles Bildmachen durch Button-Klick


Anforderungen

* Raspberry Pi Zero 2 W mit Kamera
* Server mit Linux-Betriebssystem
* Python 3.x
* Flask
* Tesseract-OCR
* OpenCV
* SQLite


Installation

1. Raspberry Pi Zero 2 W einrichten und Kamera installieren
2. Server einrichten und Python 3.x, Flask, Tesseract-OCR, OpenCV und SQLite installieren
3. Projekt-Code auf Raspberry Pi und Server kopieren
4. Cron-Job einrichten, um automatisches Bildmachen am 1. Tag im Monat um 4 Uhr durchzuführen


Verwendung

1. Raspberry Pi Zero 2 W starten und Kamera aktivieren
2. Server starten und Projekt-Code ausführen
3. Bilder vom Zählerstand aufnehmen und verarbeiten
4. Daten anzeigen und speichern
5. Manuelles Bildmachen durch Button-Klick durchführen


Code-Struktur

* `PiCode.py`: Code für Raspberry Pi Zero 2 W
* `ServerCode.py`: Code für Server
* `CronJob.py`: Code für Cron-Job
* `README.md`: Diese Datei


Lizenz

Dieses Projekt ist unter der MIT-Lizenz verfügbar.


Autor

Yannick Zanker


Version

1.0


Änderungen

* 1.0: Erste Version des Projekts


Bekannte Probleme

* Keine bekannten Probleme


Zukunftige Entwicklungen

* Verbesserung der Texterkennung und Zeigererkennung
* Hinzufügen von Benutzer-Authentifizierung und -Autorisierung
* Verbesserung der Benutzeroberfläche
