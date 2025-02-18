#!/bin/bash

# Menjalankan rasa run actions di background
rasa run actions &

# Menjalankan rasa run API
rasa run --enable-api --cors "*"
