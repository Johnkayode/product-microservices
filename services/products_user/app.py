import imp
import os
from datetime import datetime
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy




# CONFIGS

app = Flask(__name__)

DB_USER = os.environ.get("MYSQL_USER")
DB_PASS = os.environ.get("MYSQL_PASSWORD")
DB_HOST = os.environ.get("MYSQL_HOST")
DB_NAME = os.environ.get("MYSQL_DATABASE")

app.config["SQLAlchemy_DATABASE_URI"] = f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)



# MODELS
class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)

    #cart_items = db.relationship("CartItem", backref="product")


class Wishlist(db.Model):
    __tablename__ = "wishlist"
    
    # customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    id = db.Column(db.Integer, primary_key=True)
    products = db.relationship("Product", back_populates="wishlists")

class Cart(db.Model):
    __tablename__ = "cart"

    # customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    complete = db.Column(db.Boolean, default=False)
    cart_items = db.relationship("CartItem", backref="cart")
    
    @property
    def getCartTotal(self):
        return 0

class CartItem(db.Model):
    __tablename__ = "cart_item"
    
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey("cart.id"))
    cart = db.relationship("Cart")
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    product = db.relationship("Product")
    quantity = db.Column(db.Integer)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def getTotalCost(self):
        return 0

# ROUTES

@app.route("/")
def index():
    return "Hello"




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)