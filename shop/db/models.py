from shop import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String(50), nullable = False)
    pasword_hash = db.Column(db.String(220), nullable = False)
    address = db.Column(db.String(50), nullable = False)