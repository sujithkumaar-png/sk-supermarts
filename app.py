from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Product page
@app.route('/product/<int:product_id>')
def product(product_id):
    # Fetch product data here
    return render_template('product.html', product_id=product_id)

# Add to cart
@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity')
    # Add to cart logic here
    return jsonify({'message': 'Product added to cart'})

# Cart page
@app.route('/cart')
def cart():
    # Load cart items here
    return render_template('cart.html')

# Checkout
@app.route('/checkout', methods=['POST'])
def checkout():
    # Handle checkout logic here
    return jsonify({'message': 'Checkout successful'})

if __name__ == '__main__':
    app.run(debug=True)