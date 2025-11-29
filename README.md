# 🐳 Cloud-Native Flask App — Deployment mit Docker & Kubernetes

Dieses Projekt zeigt den vollständigen Weg von einer einfachen Python-Flask-Anwendung bis hin zum Deployment in einem Kubernetes-Cluster – inklusive Containerisierung, Services, NodePort-Zugriff, Deployment-Manifests und Docker-Compose.

Die Anwendung liefert eine einfache HTTP-Antwort:

```

Hello from Docker und Kubernetes! Host: <pod-name>

```

---

# 🏗️ Architekturübersicht

Das folgende Diagramm zeigt die Struktur der Container-Umgebung und des Kubernetes-Deployments:

![Kubernetes-Dashboard](Bilder%20zu%20meinem%20ersten%20Docker%20+%20Kubernetes%20Projekt/docker-container-overview.png)

---

# 📦 Technologien

| Bereich | Technologien |
|--------|--------------|
| Containerisierung | Docker, Docker-Compose |
| Orchestrierung | Kubernetes (kubectl, Deployments, Services) |
| Sprache | Python 3 + Flask |
| Infrastruktur | Docker Desktop Kubernetes Cluster |
| Deployment | NodePort Service (Port 30000) |

---

# 📁 Projektstruktur

```

📦 Projektordner
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── Bilder zu meinem ersten Docker + Kubernetes Projekt/

````

---

# 🧪 Lokale Entwicklung & Start mit Docker

### 1️⃣ Image bauen
```sh
docker build -t hello-kube .
````

### 2️⃣ Container starten

```sh
docker run -p 5000:5000 hello-kube
```

### Browser öffnen

➡ [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

# 🐙 Docker-Compose

Datei: **docker-compose.yml**

```
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
```

Starten:

```sh
docker compose up -d
```

---

# ☸️ Kubernetes Deployment

## Deployment-Manifest (`deployment.yaml`)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-kube-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-kube
  template:
    metadata:
      labels:
        app: hello-kube
    spec:
      containers:
      - name: hello-kube
        image: hello-kube:latest
        ports:
        - containerPort: 5000
```

## Service (`service.yaml`)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-kube-service
spec:
  type: NodePort
  selector:
    app: hello-kube
  ports:
    - port: 5000
      targetPort: 5000
      nodePort: 30000
```

Deployment starten:

```sh
kubectl apply -f k8s/
```

Pods anzeigen:

```sh
kubectl get pods
```

Services anzeigen:

```sh
kubectl get svc
```

---

# 🌐 Zugriff über NodePort

Nachdem der Service aktiv ist:

➡ **[http://127.0.0.1:30000/](http://127.0.0.1:30000/)**

Wenn der Pod läuft, erscheint:

```
Hello from Docker und Kubernetes! Host: hello-kube-deployment-xxxxx
```

---

# 📸 Screenshots

### ✔ Docker Desktop – Container Übersicht

![Docker Container Übersicht](Bilder%20zu%20meinem%20ersten%20Docker%20+%20Kubernetes%20Projekt/docker-container-overview.png)

---

### ✔ Kubernetes Dashboard – Cluster, Pods, Services

![Kubernetes Dashboard](Bilder%20zu%20meinem%20ersten%20Docker%20+%20Kubernetes%20Projekt/Kubernetes-dashboard-overview.png)

---

### ✔ VS Code – Projektstruktur & Dateien

![VS Code Dockerfile](Bilder%20zu%20meinem%20ersten%20Docker%20+%20Kubernetes%20Projekt/VS%20CODE%20Dockerfile.png)
![VS Code Compose](Bilder%20zu%20meinem%20ersten%20Docker%20+%20Kubernetes%20Projekt/VS%20CODE%20Docker-compose.yml.png)
![VS Code Deployment](Bilder%20zu%20meinem%20ersten%20Docker%20+%20Kubernetes%20Projekt/VS%20CODE%20deployment.yaml.png)
![VS Code Service](Bilder%20zu%20meinem%20ersten%20Docker%20+%20Kubernetes%20Projekt/VS%20CODE%20service.yaml.png)

---

# 🚀 Was dieses Projekt demonstriert

### 🔧 Docker-Kompetenzen

* Erstellung effizienter Dockerfiles
* Umgang mit Containern & Images
* Nutzung von Docker-Compose
* Verständnis von Container-Lifecycle

### ☸️ Kubernetes Grundlagen

* Deployments erstellen
* Services konfigurieren
* NodePort-Routing verstehen
* Pods überwachen
* Cluster-Objekte analysieren

---

# 🧭 Roadmap (geplante Erweiterungen)

| Feature                         | Status    |
| ------------------------------- | --------- |
| CI/CD mit GitHub Actions        | ⏳ geplant |
| Helm Chart Version              | ⏳ geplant |
| Ingress + SSL                   | ⏳ geplant |
| Deployment auf AWS EKS          | ⏳ geplant |
| Monitoring (Prometheus/Grafana) | ⏳ geplant |

---

# 👤 Autor

**Tugrul (Ihavetolearnalot)**
Cloud Engineering • DevOps • Automatisierung

---

# ⭐ Feedback & Support

Wenn dir dieses Projekt gefällt, freue ich mich über einen ⭐ Stern auf GitHub!

```

