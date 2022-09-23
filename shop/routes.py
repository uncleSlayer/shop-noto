from shop import app
from flask import render_template

@app.route("/")
@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")