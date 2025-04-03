# 🌐 Visitors Count Application

A simple Python-based web application that tracks the number of visitors using **Flask** and **Redis**. The application is containerized using **Docker** and can be easily deployed with **Docker Compose**.

---

## 🚀 Features

- **Flask Web Framework**: Serves the web application.
- **Redis**: Tracks the number of visitors.
- **Dockerized**: Easily deployable with Docker and Docker Compose.
- **Environment Variables**: Configurable Redis host for flexibility.

---

## 🛠️ Prerequisites

Before running the application, ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 📦 Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd VisitorsCount-Python
```
---
### 2. Build and Run the Application

Use docker-compose to build and start the application:

```bash
docker-compose up --build
```
---


### 3. Access the Application

Once the application is running, open your browser and navigate to:

```
http://localhost:5000
```

### 🐳 Docker Setup

Docker Compose Services
`web`: The Flask application.
`redis`: The Redis database for tracking visitor counts.
Environment Variables
`REDIS_HOST`: Configures the Redis host (default: redis).

### 📂 Project Structure

```
VisitorsCount-Python/
├── app/
│   ├── [app.py](http://_vscodecontentref_/0)               # Main Flask application
│   ├── [requirements.txt](http://_vscodecontentref_/1)     # Python dependencies
├── [docker-compose.yml](http://_vscodecontentref_/2)       # Docker Compose configuration
├── Dockerfile               # Dockerfile for the Flask app

```

### 🧪 Testing the Application

1.Start the application using `docker-compose`.

2.Visit the application in your browser at `http://localhost:5000`.

3.Refresh the page to see the visitor count increment.


## 🛡️ License
This project is licensed under the *MIT License*. Feel free to use and modify it as needed.
