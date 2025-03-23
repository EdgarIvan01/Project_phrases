# Nombre del Proyecto

Este proyecto es una aplicación web que utiliza un frontend basado en **Nginx** y un backend desarrollado con **Python Flask**. Ambos componentes están dockerizados para facilitar su despliegue y manejo.

## Estructura del Proyecto

El proyecto está dividido en dos partes principales:

1. **Frontend**: Servido desde un contenedor Docker basado en la imagen `nginx:alpine`.
2. **Backend**: Desarrollado en Python usando Flask y ejecutado en un contenedor Docker.

## Requisitos Previos

- Docker instalado en tu máquina.
- Docker Compose (opcional, pero recomendado para manejar múltiples contenedores).

## Configuración del Proyecto

### 1. Frontend (Nginx)

El frontend está construido usando la imagen `nginx:alpine`. Los archivos estáticos (HTML, CSS, JS) se sirven directamente desde Nginx.

- **Dockerfile** (para el frontend):
  ```Dockerfile
  FROM nginx:alpine
  COPY ./frontend /usr/share/nginx/html
  EXPOSE 80
  CMD ["nginx", "-g", "daemon off;"]
  ```

  La carpeta `frontend` contiene los archivos estáticos que se sirven al cliente.

### 2. Backend (Python Flask)

El backend está desarrollado en Python usando el framework Flask. Se ejecuta en un contenedor Docker.

- **Dockerfile** (para el backend):
  ```Dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY . .
  EXPOSE 5000
  CMD ["python", "app.py"]
  ```
- El archivo `app.py` contiene la lógica del servidor Flask.
- El archivo `requirements.txt` contiene las dependencias de Python necesarias.


  ### 3. Docker Compose (opcional)

Para facilitar el manejo de ambos contenedores, puedes usar Docker Compose. Aquí tienes un ejemplo de un archivo `docker-compose.yml`:

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
### Ejecución
1. Clona este repositorio en tu máquina local.

```cmd
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```
2. Construye y ejecuta los contenedores usando Docker Compose:

```cmd
docker-compose up --build
```
3. Accede a la aplicación:

Frontend: Abre tu navegador y visita http://localhost.

Backend: Puedes acceder a la API en http://localhost:5000.

3. Accede a la aplicación:
   - Frontend: Abre tu navegador y visita `http://localhost`.
   - Backend: Puedes acceder a la API en `http://localhost:5000`.

## Estructura de Carpetas

```txt
tu-repositorio/
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
