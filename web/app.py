from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Rute untuk halaman utama
@app.route("/")
def index():
    return render_template("index.html")  # Mengembalikan file index.html

# Rute untuk chat
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # Kirim pesan ke Rasa untuk mendapatkan respons
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"  # URL API Rasa
    payload = {"sender": "user", "message": user_message}
    response = requests.post(rasa_url, json=payload)

    # Ambil respons dari Rasa
    rasa_response = response.json()
    print("Rasa response:", rasa_response)

    # Kirim respons kembali ke pengguna
    return jsonify({"response": rasa_response})

if __name__ == "__main__":
    app.run(port=5000)
