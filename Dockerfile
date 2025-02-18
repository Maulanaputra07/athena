FROM rasa/rasa:latest
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["rasa", "run", "--enable-api", "--cors", "*"]
# Mengatur virtual environment
# Mengupgrade pip
RUN pip install --upgrade pip

RUN pip uninstall confluent-kafka

# Install dependensi
RUN pip install -r requirements.txt
