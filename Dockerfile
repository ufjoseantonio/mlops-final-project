# 1. Usamos la imagen oficial de Python ligera
FROM python:3.11-slim

# 2. Carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos SOLO los requerimientos ligeros de la API
COPY requirements_api.txt .

# 4. Instalamos las librerías
RUN pip install --no-cache-dir -r requirements_api.txt

# 5. Copiamos el código de la API y la carpeta del modelo
COPY src/ src/
COPY models/ models/

# 6. Exponemos el puerto de Flask
EXPOSE 5000

# 7. Encendemos el motor de inferencia
CMD ["python", "src/serving.py"]