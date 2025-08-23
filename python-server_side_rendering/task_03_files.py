from flask import Flask, render_template, request
import json
import csv

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


@app.route('/items')
def items():
    filename = "./data/items.json"
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            items = json.loads(f.read())["items"]
    except (FileNotFoundError, KeyError):
        items = []
    return render_template('items.html', items=items)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    items = []
    message = None

    if source in ['json', 'csv']:
        filename = f"./products.{source}"
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                if source == 'json':
                    items = json.load(f)
                else:
                    reader = csv.DictReader(f)
                    items = [row for row in reader]
                    # convert id to int for consistency
                    for item in items:
                        item["id"] = int(item["id"])
                        item["price"] = float(item["price"])
        except FileNotFoundError:
            message = "File not found"
            items = []

        # if filtering by ID
        if product_id:
            try:
                product_id = int(product_id)
                items = [item for item in items if item["id"] == product_id]
                if not items:
                    message = "Product not found"
            except ValueError:
                message = "Invalid product ID"

    else:
        message = "Wrong source"

    return render_template('product_display.html', items=items, message=message)



if __name__ == '__main__':
    app.run(debug=True, port=5000)