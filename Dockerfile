# Menggunakan image Rasa terbaru sebagai base image
FROM rasa/rasa:latest

# Menyalin semua file ke dalam container
COPY . /app
WORKDIR /app

# Menjalankan perintah dengan hak akses root
USER root

# Menyalin file start.sh ke dalam container
COPY start.sh /app/start.sh

# Memberikan izin eksekusi pada start.sh
RUN chmod +x /app/start.sh

# Menjalankan skrip start.sh
CMD ["/app/start.sh"]

# Memastikan pip sudah terinstal dan mengupgradenya
RUN python -m ensurepip --upgrade && \
    pip install --upgrade pip --no-cache-dir

# Menghapus confluent-kafka jika sebelumnya sudah terinstal (jika diperlukan)
RUN pip uninstall -y confluent-kafka

# Install dependensi dari requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

# Menjalankan Rasa server dengan opsi API dan CORS yang diizinkan
CMD ["rasa", "run", "--enable-api", "--cors", "*"]
