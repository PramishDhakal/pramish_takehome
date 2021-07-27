from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)

app.config['SQLAlchemy_DATABASE_URI'] = 'mysql://root:root@localhost:33067/main'
SQLALCHEMY_TRACK_MODIFICATIONS = False

CORS(app)

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.Integer)
    image = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/')
def home():
    return 'This is my take home exam'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
