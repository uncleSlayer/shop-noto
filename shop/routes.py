from crypt import methods
from itertools import product
from flask_login import current_user, login_required, login_user, logout_user
from shop import app, bcrypt_app
from flask import jsonify, render_template, request, session, url_for, redirect
from shop.database.model import Cart_items, Products

# index, shop
@app.route("/")
@app.route("/shop")
@login_required
def shop():
    from shop.database.model import Products
    all_products = Products.query.all() 
    return render_template("shop.html", products = all_products)


# signup
@app.route("/signup", methods = ['GET', 'POST'])
def signup_form():
    from shop.database.model import Users
    from shop import db
    try:
        if request.method == 'POST':

            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            re_password = request.form['repassword']

            print(email)

            if password == re_password:

                check_user = Users.query.filter_by(email = email).first()

                if check_user:
                    print(check_user)
                    print('user with this email address already exist')
                    return render_template('signup.html')
                else:

                    hashedpw = bcrypt_app.generate_password_hash(password=password).decode('utf-8')
                    # print(bcrypt_app.check_password_hash(pw_hash=hashedpw, password=password))
                    user = Users(username = name, email = email, password_hash = hashedpw)

                    db.session.add(user)
                    db.session.commit()

            else:

                print('password did not match')
                return render_template('signup.html')

            return redirect(url_for('login_form'))
    except Exception as e:
        print(e)

    return render_template("signup.html")


# loign
@app.route("/login", methods = ['GET', 'POST'])
def login():
    from shop.database.model import Users
    from shop.database.model import Products

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = Users.query.filter_by(email = email).first()

        print(user)

        try:
            if bcrypt_app.check_password_hash(pw_hash = user.password_hash, password = password):
                try:
                    login_user(user=user)
                    print(current_user)
                    return redirect(url_for('shop'))
                except Exception as e:
                        print(e)
        except Exception as e:
            print(e)
            
    return render_template('login.html')

# cart
@app.route("/cart")
@login_required
def cart():
    from shop.database.model import Users, Products, Cart, Cart_items

    products = Cart.query.filter(Cart.user_id == current_user.id).all()

    product_data_front_end = []

    for item in products:
        product_qty = Cart_items.query.filter(Cart_items.cart_id == item.id).first()

        product_name_obj = Products.query.filter(Products.id == item.product_id).first()
        product_name = product_name_obj.name

        product_object = {
            'product_name': product_name,
            'product_qty': product_qty.quantity
        }

        product_data_front_end.append(product_object)

    print(product_data_front_end)


    return render_template("cart.html", product_det = product_data_front_end)

# logout
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# add to cart api
@app.route('/cart-add', methods = ['GET', 'POST'])
def cart_adder():
    from shop import db
    from shop.database.model import Products, Cart, Cart_items

    req = request.get_json()
    cart_name = req['cart_name']
    cart_value = req['cart_value']

    product = Products.query.filter_by(name = cart_name).first()

    print(product.name)

    cart = Cart.query.filter(Cart.user_id == current_user.id, Cart.product_id == product.id).first()
    cart = Cart.query.filter(Cart.user_id == current_user.id, Cart.product_id == product.id).first()

    print(cart)

    if cart == None:
        new_cart = Cart(user_id = current_user.id, product_id = product.id)

        db.session.add(new_cart)
        db.session.commit()

        new_cart_item = Cart_items(quantity = cart_value)

        new_cart.cart_items.append(new_cart_item)

        db.session.add(new_cart_item)

        db.session.commit()

    else:

        existing_cart_item = Cart_items.query.filter(Cart_items.cart_id == cart.id).first()

    
        qty = existing_cart_item.quantity

        existing_cart_item.quantity = int(qty) + int(cart_value)

        db.session.commit()

    return jsonify({
        'message': 'worked perfectly',
        'data sent': req
    })

    # create order
@app.route('/make-order', methods = ['post'])
def create_order():

    # cart_items = Cart_items.query.filter(Cart_items.)

    return jsonify({
        'message': 'order created successfully'
    })