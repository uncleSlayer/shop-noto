from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:sid00100@web-noto-dep.cbsshr86luzi.ap-south-1.rds.amazonaws.com:5432/webnoto"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET'] = 'supersecretkey'
app.secret_key = 'super secret key'

db = SQLAlchemy(app)
bcrypt_app = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    from shop.database.model import Users
    user = Users.query.filter(Users.id == user_id).first()
    if user:
        return user
    else:
        pass
