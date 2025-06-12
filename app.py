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
