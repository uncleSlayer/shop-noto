from shop import app
from flask import render_template

@app.route("/")
@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/signup", methods = ['GET'])
def signup_form():
    return render_template("signup.html")


@app.route("/login")
def login_form():
    return render_template("login.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")