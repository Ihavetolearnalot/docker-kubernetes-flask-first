# wir importieren von "flask" wo unser Webserver ist, das FLASK-Framework, um einen kleinen Webserver zu bauen
from flask import Flask

# socket benutzen wir, um den Hostnamen auszulesen
import socket

# hier erstelle ich eine Flask-App. __name__ sagt Flask, wo es starten soll.
# Was ist eine Flask-App? Das ist ein kleiner Webserver.
app = Flask(__name__)

# das ist die Startseite (Route "/") unserer Web-App
# wenn jemand die Startseite aufruft, wird die Funktion index() ausgeführt
@app.route('/')
def index():
    # der Hostname ist später der Name des Containers / Pods in Kubernetes
    hostname = socket.gethostname()

    # wir geben einen Text zurück, der im Browser erscheint
    return f'Hello from Docker und Kubernetes! Host: {hostname}!'

# Dieser Block sorgt dafür, dass die App gestartet wird, wenn wir das Skript direkt ausführen
# ohne das würde Flask in manchen Umgebungen doppelt starten
if __name__ == '__main__':
    # Flask startet standardmäßig auf 127.0.0.1 (nur lokal erreichbar)
    # Wir wollen aber, dass die App von außen erreichbar ist, also auf 0.0.0.0
    # Port 5000 ist der Standardport für Flask
    app.run(host='0.0.0.0', port=5000)