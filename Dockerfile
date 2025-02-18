# Menggunakan image Rasa terbaru sebagai base image
FROM rasa/rasa:latest

# Menyalin semua file ke dalam container
COPY . /app
WORKDIR /app

# Menjalankan perintah dengan hak akses root
USER root

# Memastikan pip sudah terinstal dan mengupgradenya
RUN python -m ensurepip --upgrade && \
    pip install --upgrade pip --no-cache-dir

# Menghapus confluent-kafka jika sebelumnya sudah terinstal (jika diperlukan)
RUN pip uninstall -y confluent-kafka

# Install dependensi dari requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

# Menjalankan server Rasa dengan API dan CORS, dan actions di background
CMD ["bash", "-c", "rasa run --enable-api --cors '*' & rasa run actions"]
