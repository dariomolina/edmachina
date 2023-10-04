# Utiliza la imagen oficial de Python como base
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos e instala las dependencias
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && adduser --disabled-password --no-create-home edmachina

USER edmachina 

# Copia el código de la aplicación en el contenedor
COPY . .

# Expone el puerto en el que la aplicación FastAPI estará escuchando
EXPOSE 8000

# Comando para iniciar la aplicación FastAPI
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
