FROM rasa/rasa:latest
<<<<<<< HEAD
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
=======

COPY . /app
WORKDIR /app
# Mengatur virtual environment
# Mengupgrade pip


RUN pip install --upgrade pip

RUN pip uninstall confluent-kafka

# Install dependensi
RUN pip install -r requirements.txt


>>>>>>> 6010ce1e787c39df3bba799b3c71dbacdf1aee8d
CMD ["rasa", "run", "--enable-api", "--cors", "*"]
