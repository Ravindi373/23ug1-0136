# Dockerized Flask & MySQL Web App

A containerized web application built with **Flask** and **MySQL**, orchestrated using **Docker Compose**, and deployed live on **Railway**. The app connects to a MySQL database, logs each visit, and displays a running visit counter — demonstrating multi-container orchestration, persistent storage, and container networking with Docker.

**🔗 Live Demo:** [mysql-docker-flask-production.up.railway.app](https://mysql-docker-flask-production.up.railway.app)

---

## Tech Stack

* **Docker** – Runs the application inside isolated containers.
* **Docker Compose** – Manages and orchestrates multiple containers together (local development).
* **Python & Flask** – Backend web framework serving the application.
* **MySQL 8.0** – Relational database used to store and persist visit records.
* **Railway** – Cloud platform used for live deployment of both the app and the database.

---

## Application Description

The application is a small Flask web service that connects to a MySQL database. On every page load, the app:

1. Connects to the MySQL database (with automatic retry logic in case the database is still starting up).
2. Creates a `visits` table if it doesn't already exist.
3. Inserts a new visit record.
4. Returns the total number of visits recorded so far, rendered on a styled HTML page.

---

## Network and Volume Details (Local / Docker Compose)

* **Networks**: An external Docker network (`app-net`) is created so the `web` and `db` containers can communicate with each other securely.
* **Volumes**: A named external volume (`db-data`) is used to persist MySQL data, ensuring data is not lost when containers stop or are removed.

---

## Container Configuration

* Each service is defined in `docker-compose.yaml`.
* Containers are configured with specific ports, environment variables, and network settings.
* Both services are connected to the same Docker network (`app-net`) for internal communication.
* Database credentials are supplied via environment variables (see **Environment Setup** below) rather than hardcoded in the compose file.

---

## Container List

1. **Web Container** – Runs the Flask application, listens on port `5000`.
2. **DB Container** – Runs MySQL 8.0, stores application data persistently via the `db-data` volume.

---

## Project Structure

```
mysql-docker-flask/
├── app.py
├── Dockerfile
├── requirements.txt
├── docker-compose.yaml
├── prepare-app.sh
├── start-app.sh
├── stop-app.sh
├── remove-app.sh
├── .env.example
└── README.md
```

---

## Environment Setup

Before running the app locally, create a `.env` file in the project root (copy `.env.example` and fill in your own values):

```bash
cp .env.example .env
```

`.env.example`:
```
DB_USER=root
DB_PASSWORD=example
DB_NAME=mydb
MYSQL_ROOT_PASSWORD=example
```

> **Note:** The `.env` file is excluded from version control via `.gitignore` and should never be committed with real credentials.

---

## Steps to Run Locally

```bash
# 1. Prepare environment (creates network/volume, builds Docker images)
./prepare-app.sh

# 2. Start the application (runs containers in the background)
./start-app.sh

# 3. Stop the application (stops containers but keeps data)
./stop-app.sh

# 4. Remove the application (cleans up containers, images, and volumes)
./remove-app.sh
```

Once running locally, the app is available at:

```
http://localhost:5000
```

Each time the page is refreshed, the visit counter increments, confirming that data is being written to and read from the persistent MySQL volume.

---

## Live Deployment

This app is also deployed on **Railway**, with both the Flask web service and a managed MySQL database running as separate services within the same project, connected over Railway's internal networking. Environment variables (`DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`) are securely injected via Railway's variable references, and the service is exposed on a public Railway-provided domain with automatic SSL.

**Live URL:** [https://mysql-docker-flask-production.up.railway.app](https://mysql-docker-flask-production.up.railway.app)

---

## Author
Ravindi Ayodhya - 
Built as part of the CCS3308 coursework, demonstrating Docker containerization, multi-service orchestration with Docker Compose, and cloud deployment with a live, persistent database.
