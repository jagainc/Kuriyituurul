from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def home():
    with open("code_snippets.json") as f:
        snippets = json.load(f)
    return render_template("index.html", snippets=snippets)

if __name__ == "__main__":
    app.run(debug=True)
