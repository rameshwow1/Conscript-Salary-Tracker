from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

db = None


def get_app():
	global db
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'alsdkfjalsdkfj'
	# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

	file_path = os.path.abspath(os.getcwd())+"/db.sqlite"
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
 	db = SQLAlchemy(app)
	
	# db.init_app(app)
	login_manager = LoginManager()
	login_manager.login_view = 'login'
	login_manager.init_app(app)
	from models import User

	@login_manager.user_loader
	def load_user(user_email):
		return User.query.get(user_email)
	return app
