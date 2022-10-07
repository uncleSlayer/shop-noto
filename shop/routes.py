from flask_login import current_user, login_required, login_user, logout_user
from shop import app, bcrypt_app
from flask import jsonify, render_template, request, session, url_for, redirect

from shop.database.model import Products


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

            if password == re_password:

                check_user = Users.query.filter(email == email).first()

                if check_user:
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
    all_products = Products.query.all() 

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = Users.query.filter(email == email).first()

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
    return render_template("cart.html")

# logout
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))