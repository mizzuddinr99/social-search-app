# social-search-app

✅ Fungsi:
Input: nama atau kata kunci
Dropdown: pilih platform (Facebook, Instagram, TikTok, Twitter)
Output: hasil carian daripada Google berdasarkan dork

📁 Struktur Fail

social_search_app/
│
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # Frontend HTML
├── .env                    # Simpan API Key (rahsia)
└── requirements.txt        # Keperluan Python

📦 requirements.txt

flask
requests
python-dotenv

🔐 .env (tidak perlu upload ke GitHub)

GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_custom_search_engine_id

🔙 app.py – Flask Backend

from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

def google_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": query
    }
    response = requests.get(url, params=params)
    results = response.json().get("items", [])
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        keyword = request.form["keyword"]
        platform = request.form["platform"]
        dork_query = f"site:{platform}.com {keyword}"
        results = google_search(dork_query)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
    
🌐 templates/index.html – Frontend

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Social Search</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="p-4">
    <div class="container">
        <h1 class="mb-4">Carian Media Sosial (Google Dorking)</h1>
        <form method="POST">
            <div class="mb-3">
                <input type="text" name="keyword" class="form-control" placeholder="Masukkan nama atau kata kunci" required>
            </div>
            <div class="mb-3">
                <select name="platform" class="form-control" required>
                    <option value="facebook">Facebook</option>
                    <option value="instagram">Instagram</option>
                    <option value="tiktok">TikTok</option>
                    <option value="twitter">Twitter</option>
                </select>
            </div>
            <button class="btn btn-primary" type="submit">Cari</button>
        </form>

        {% if results %}
        <hr>
        <h4>Keputusan:</h4>
        <ul class="list-group mt-3">
            {% for item in results %}
                <li class="list-group-item">
                    <a href="{{ item.link }}" target="_blank"><strong>{{ item.title }}</strong></a><br>
                    {{ item.snippet }}
                </li>
            {% endfor %}
        </ul>
        {% endif %}
    </div>
</body>
</html>

🚀 Langkah Akhir: Jalankan App

pip install -r requirements.txt
python app.py


--- Kemudian buka browser ke http://127.0.0.1:5000
