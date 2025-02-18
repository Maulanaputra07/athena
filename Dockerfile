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

# Membuat file start.sh untuk menjalankan Rasa dengan API dan actions
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Menjalankan start.sh yang mengatur eksekusi Rasa dan actions
ENTRYPOINT ["/bin/bash", "/start.sh"]
