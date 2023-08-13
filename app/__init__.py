from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin

server = Flask(__name__)
dbase = SQLAlchemy(server)

server.config['SECRET_KEY'] = 'secretsecretsecret'
server.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://twsdfwndsrgudp:f5ab35f7f88c69671ffff47fe2e8050dc7b4651ccc8c72dd4235b59b567e6f5a@ec2-44-213-228-107.compute-1.amazonaws.com:5432/d27bhnpl38ckha'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(server)

from app.models import *
from app.forms import *
from app.routes import *

dbase.create_all()