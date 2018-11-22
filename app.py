from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
import db
from business import Cart
def create_app():
  app = Flask(__name__, static_folder='C:/Users/mgabb2015/source/repos/murach/python/book_apps/ch16/shopping_cart/templates/static')
  Bootstrap(app)
  app.config['SECRET_KEY'] = 'devkey'
  return app
app = create_app()
appCart = Cart()


@app.route("/", methods =('GET', 'POST'))
def index():
    categories = db.get_categories()
    return render_template('header.html', content = categories, cart = appCart)

@app.route("/products", methods=['POST', 'GET'])
def allProd():
    if request.method == 'POST':
        if "Add_To_Cart" in request.form:
            addToCart(request.form['Add_To_Cart'])
        elif "Remove_From_Cart" in request.form:
            removeFromCart(request.form['Remove_From_Cart'])

    products = db.get_products()
    categories = db.get_categories()
    return render_template('products.html', content = products, content2 = categories, cart = appCart)

@app.route("/products/<category>",methods=['POST', 'GET'])
def prodByCategory(category, methods=['POST', 'GET']):
    if request.method == 'POST':
        if "Add_To_Cart" in request.form:
            addToCart(request.form['Add_To_Cart'])
        elif "Remove_From_Cart" in request.form:
            removeFromCart(request.form['Remove_From_Cart'])

    products = db.get_products_by_category(category)
    categories = db.get_categories()
    return render_template('products.html', content = products, content2 = categories, cart = appCart)

@app.route("/cart", methods=['POST', 'GET'])
def cartProd():
    if request.method == 'POST':
        if "Add_To_Cart" in request.form:
            addToCart(request.form['Add_To_Cart'])
        elif "Remove_From_Cart" in request.form:
            removeFromCart(request.form['Remove_From_Cart'])
    products = appCart.getProducts()
    return render_template('products.html', content = products, cart = appCart, cartPage = 1)

@app.route("/checkout", methods=['POST', 'GET'])
def checkout():
    if request.method == 'POST':
        if "Add_To_Cart" in request.form:
            addToCart(request.form['Add_To_Cart'])
        elif "Remove_From_Cart" in request.form:
            removeFromCart(request.form['Remove_From_Cart'])
    products = appCart.getProducts()
    return render_template('checkout.html', content = products, cart = appCart)

def addToCart(ID):
    product = db.getProductByID(ID)
    appCart.addItem(product)

def removeFromCart(ID):
    product = db.getProductByID(ID)
    appCart.removeItem(product)

if __name__ == "__main__":
    app.run()