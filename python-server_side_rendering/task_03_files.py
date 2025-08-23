import json
import csv
import os
from flask import Flask, render_template, request
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

@app.route("/products")
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    file_path = ''

    if source == 'json':
        file_path = 'products.json'

    elif source == 'csv':
        file_path = 'products.csv'
    else:
        return render_template('product_display.html', error="Wrong source")

    if not os.path.exists(file_path):
        return render_template('product_display.html', error="File not found")

    if source == 'json':
        products = read_json(file_path)
    else:
        products = read_csv(file_path)

    if product_id:
        product_id = int(product_id)
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)
if __name__ == '__main__':
    app.run(debug=True, port=5000)

