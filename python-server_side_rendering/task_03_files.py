from flask import Flask, render_template
import csv
import json

app = Flask(__name__)

@app.route('/sourcess')
def sources(source, id):
    if source == 'json':
        with open('products.json', 'r') as f:
            products = json.load(f) 
    elif source == 'csv':
        products = []
        with open('products.csv', 'r') as f:
            csvFile = csv.DictReader(f)
            for lines in csvFile:
                products.append(lines)
    else:
        return "Wrong source"
    
    if id:
        filtered_products = [product for product in products if product.get('id') == id]
    else:
        filtered_products = products

    return render_template('product_display.html', products=filtered_products)