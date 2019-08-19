from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '1289f249a1e29403e0cbbe3656ce4569'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from application import routes