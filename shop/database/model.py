from shop import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True)
    email = db.Column(db.String(50), unique = True)
    password_hash = db.Column(db.String(500), unique = True)
    address = db.Column(db.String(50))
    cart = db.relationship('Cart', backref = 'cart_user')
    order = db.relationship('Order', backref = 'order_user')

class Products(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True)
    desc = db.Column(db.String(350))
    price = db.Column(db.Integer)
    cart = db.relationship('Cart', backref = 'cart_product')
    order = db.relationship('Order', backref = 'order_product')


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    cart_items = db.relationship('Cart_items', backref = 'cart')

class Cart_items(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    quantity = db.Column(db.Integer)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    order_item = db.relationship('Order_items', backref = 'order')

class Order_items(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    quantity = db.Column(db.Integer)