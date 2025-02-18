#!/bin/bash
# Menjalankan Action Server di background
rasa run actions &

# Menjalankan Rasa Server
rasa run --enable-api --cors "*"
