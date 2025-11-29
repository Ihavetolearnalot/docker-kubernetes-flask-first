# 1. Basis-Image: offizielles Python-Image
FROM python:3.12-slim

# 2. Arbeitsverzeichnis im Container
WORKDIR /app

# 3. Requirements in den Container kopieren
COPY requirements.txt /app/

# 4. Python-Pakete im Container installieren
RUN pip install --no-cache-dir -r requirements.txt

# 5. Restliche Dateien in den Container kopieren
COPY . /app

# 6. Port, auf dem Flask im Container lauscht
EXPOSE 5000

# 7. Startbefehl für die Anwendung
CMD ["python", "app.py"]