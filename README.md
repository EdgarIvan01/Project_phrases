# Project phrase

This project is a web application that uses a frontend based on **Nginx** and a backend developed with **Python Flask**. Both components are Dockerized for easy deployment and management.

## Project Structure

The project is divided into two main parts:

1. **Frontend**: Served from a Docker container based on the `nginx:alpine` image.
2. **Backend**: Developed in Python using Flask and running in a Docker container.

## Prerequisites

- Docker installed on your machine.
- Docker Compose (optional, but recommended for managing multiple containers).

## Project Configuration

### 1. Frontend (Nginx)

The frontend is built using the `nginx:alpine` image. Static files (HTML, CSS, JS) are served directly from Nginx.

- **Dockerfile** (for the frontend):
```Dockerfile
FROM nginx:alpine
COPY ./frontend /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

The `frontend` folder contains the static files served to the client.

### 2. Backend (Python Flask)

The backend is developed in Python using the Flask framework. It runs in a Docker container.

- **Dockerfile** (for the backend):
```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```
- The `app.py` file contains the Flask server logic.
- The `requirements.txt` file contains the necessary Python dependencies.

### 3. Docker Compose

To make it easier to manage both containers, you can use Docker Compose. Here's an example of a `docker-compose.yml` file:

```yaml
version: '3'
services:
frontend:
build: ./frontend
ports:
- "80:80"
depends_on:
- backend

backend:
build: ./backend
ports:
- "5000:5000"
```
### Execution
1. Clone this repository to your local machine.

```cmd
git clone https://github.com/your-user/your-repository.git
cd your-repository
```
2. Build and run the containers using Docker Compose:

```cmd
docker-compose up --build
```
3. Access the application:
- Frontend: Open your browser and visit `http://localhost`.
- Backend: You can access the API at `http://localhost:5000`.

## Folder Structure

```txt
your-repository/
├── frontend/
│ ├── Dockerfile
│ ├── index.html
│ ├── styles.css
│ └── script.js
├── backend/
│ ├── Dockerfile
│ ├── app.py
│ └── requirements.txt
└── docker-compose.yml
```
