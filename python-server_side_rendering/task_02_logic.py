import json
from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/items")
def items():
    data_path = Path(__file__).with_name("items.json")
    try:
        items_list = json.loads(data_path.read_text(encoding="utf-8")).get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template("items.html", items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)