# 1. Imagen base de Python (versión ligera para que no pese mucho)
FROM python:3.11-slim

# 2. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Instalamos dependencias del sistema necesarias para PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 4. Copiamos el requirements.txt que creamos antes
COPY requirements.txt .

# 5. Instalamos las librerías de Python (Flask, SQLAlchemy, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiamos todo el contenido de la carpeta 'backend' al contenedor
COPY . .

# 7. Exponemos el puerto 5000 (el que usa Flask por defecto)
EXPOSE 5000

# 8. El comando para arrancar tu aplicación
CMD ["python", "app.py"]