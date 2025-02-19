#!/bin/bash
# Menjalankan Rasa dengan API dan CORS, dan actions di background
rasa run --enable-api --cors "*" --port ${PORT:-5005} &
rasa run actions --port 5055
wait
