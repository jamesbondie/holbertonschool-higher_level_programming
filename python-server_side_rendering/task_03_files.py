from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')

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
        products = [product for product in products if product.get('id') == id]
        if not products:
            print("Product not found")
    else:
        products = products

    return render_template('product_display.html', products=products)



if __name__ == '__main__':
    app.run(debug=True, port=5000)