FROM python:3.10-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libgdk-pixbuf2.0-0 \
    libxrender1 \
    libxext6 \
    libsm6 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY video/ /app/video/
COPY timed_camera.py .

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "timed_camera.py", "--server.port=8501", "--server.address=0.0.0.0"]
