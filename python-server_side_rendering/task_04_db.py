from flask import Flask, render_template, request
import json
import csv
import sqlite3

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
    # Read items from JSON file
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    
    source = request.args.get('source')
    product_id = request.args.get('id', type=int) 

    product_data = []
    headers = []
    error_message = None

   
    if source not in ['json', 'csv', 'sql']:
        error_message = "Wrong source"
        return render_template('product_display.html',
                            products=product_data,
                            headers=headers,
                            error_message=error_message)

  
    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                product_data = json.load(f)
                headers = list(product_data[0].keys())
        except (FileNotFoundError, json.JSONDecodeError):
            error_message = "File not found"
    elif source == 'csv':
        try:
            with open('products.csv', 'r') as f:
                reader = csv.DictReader(f)
                product_data = list(reader)
                headers = list(product_data[0].keys())
        except FileNotFoundError:
            error_message = "File not found"
    elif source == 'sql':
        conn = None
        try:
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT id, name, category, price FROM Products')
            rows = cursor.fetchall()
           
            for row in rows:
                product_data.append({
                    'id': row['id'],
                    'name': row['name'],
                    'category': row['category'],
                    'price': row['price']
                })
            headers = list(product_data[0].keys())
        except sqlite3.Error:
            error_message = "File not found"
        finally:
            if conn:
                conn.close()

    # Filter by id
    if product_id is not None:
        filtered_products = []
        for product in product_data:
            if product.get('id') == product_id:
                filtered_products.append(product)
        if not filtered_products:
            error_message = "Product not found"
            product_data = []
        else:
            product_data = filtered_products

    return render_template('product_display.html', products=product_data,
                           headers=headers, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)