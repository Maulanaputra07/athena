# Gunakan image resmi Rasa
FROM rasa/rasa:latest

# Set working directory di dalam container
WORKDIR /app

# Copy semua file proyek ke dalam container
COPY . /app

# Install dependencies jika ada custom actions
RUN pip install -r requirements.txt || true

# Train model Rasa
RUN rasa train

# Jalankan Rasa
CMD ["rasa", "run", "--enable-api", "--cors", "*"]
