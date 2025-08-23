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
    id = request.args.get('id')
    items = []
    message = None

    if source in ['json', 'csv']:
        filename = f"./products.{source}"
        with open(filename, 'r', encoding="utf-8") as f:
            if source == 'json':
                items = json.loads(f.read())
            else:
                dictionaries = csv.DictReader(f)
                for item in dictionaries:
                    items.append(item)
        if id:
            id = int(id)
            valid = [item["id"] for item in items]
            print(valid)
            if id not in valid:
                print(id)
                message = "Product not found"
    else:
        message = "Wrong source"

    return render_template('product_display.html', items=items, id=id, message=message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)