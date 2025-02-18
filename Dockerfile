FROM rasa/rasa:latest
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["rasa", "run", "--enable-api", "--cors", "*"]
