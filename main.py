from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def get_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'alsdkfjalsdkfj'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
	db.init_app(app)
	login_manager = LoginManager()
	login_manager.login_view = 'login'
	login_manager.init_app(app)
	from models import User

	@login_manager.user_loader
	def load_user(user_email):
		return User.query.get(user_email)
	return app
