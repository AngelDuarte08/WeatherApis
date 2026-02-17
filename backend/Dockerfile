FROM python:3.13-slim
WORKDIR /app


RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Instalamos gunicorn explícitamente por si no está en requirements.txt
RUN pip install gunicorn

EXPOSE 5008


CMD ["gunicorn", "--bind", "0.0.0.0:5008", "run:app"]