from flask import Flask
from extentions import*
import config

from models.user import User
from models.cart import Cart
from models.product import Product
from models.cart_item import CartItem


from blueprints.general import app as general
from blueprints.admin import app as admin
from blueprints.user import app as user

app = Flask(__name__)
app.register_blueprint(general)
app.register_blueprint(admin)
app.register_blueprint(user)



app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = config.SECRET_KEY
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=8085)