# Anleitung zur Konfiguration des Cronjobs
# --------------------------------------------------------

# 1. Öffne die Cronjob-Datei in einem Editor
#    crontab -e (als normaler Benutzer)
#    sudo nano /etc/crontab (als Root-Benutzer)

# 2. Füge den folgenden Eintrag hinzu:
#    0 4 1 * * python /home/server/cron_job.py
#    Dieser Eintrag führt das Python-Skript /home/server/cron_job.py
#    jeden 1. Tag des Monats um 4:00 Uhr aus.

# 3. Speichere die Änderungen und schließe den Editor

# 4. Stelle sicher, dass das Python-Skript /home/server/cron_job.py
#    existiert und ausführbar ist.

# 5. Überprüfe, ob der Cronjob korrekt konfiguriert ist, indem du
#    den folgenden Befehl ausführst:
#    crontab -l (als normaler Benutzer)
#    sudo crontab -l (als Root-Benutzer)

# 6. Wenn alles korrekt konfiguriert ist, sollte der Cronjob
#    jeden 1. Tag des Monats um 4:00 Uhr das Python-Skript
#    /home/server/cron_job.py ausführen.

# Cronjob-Datei
# -------------
0 4 1 * * python /home/server/cron_job.py