from main import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
	email = db.Column(db.String(100), unique=True, primary_key=True)
	password = db.Column(db.String(100))
