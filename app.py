import os
os.system('python3.12 -m venv ./venv')
os.system('source venv/bin/activate')
os.system('pip3 install flask, flask_login, flask_sqlalchemy, pymongo')
os.system('pip3 uninstall werkzeug')
os.system('pip3 install werkzeug==2.3.0')
os.system('python3.12 app.py')
from flask import request, render_template, redirect
import main
from logic import average_salary
from main import db
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

app = main.get_app()

with app.app_context():
	db.create_all()

islogged = False
avgsal = 'Not Defined'


@app.route('/')
def home():  # put application's code here
	global islogged, avgsal
	return render_template('home.html', islogged=islogged, avgsal=avgsal)


@app.route('/', methods=['POST'])
@login_required
def getavg():
	global avgsal
	uskill = request.form.get('user-skill')
	uquali = request.form.get('user-quali')
	uloc = request.form.get('user-loc')
	uminexp = request.form.get('user-min-exp')
	umaxexp = request.form.get('user-max-exp')
	avgsal = average_salary(uskill, uquali, uloc, uminexp, umaxexp)
	return redirect('/')


@app.route('/login', methods=['POST'])
def login():
	global islogged
	email = request.form.get('login-email')
	passw = request.form.get('login-pass')
	user = User.query.filter_by(email=email).first()
	if not user or not check_password_hash(user.password, passw):
		return '<script>alert("Email - Password is Incorrect!"); open("http://127.0.0.1:5000/", "_self")'
	login_user(user, True)
	islogged = True
	return redirect('/')


@app.route('/logout')
@login_required
def logout():
	global islogged
	logout_user()
	islogged = False
	return redirect('/')


@app.route('/signup', methods=['POST'])
def signup():
	global islogged
	email = request.form.get('signup-email')
	passw = request.form.get('signup-pass')
	user = User.query.filter_by(email=email).first()
	if user:
		return '<script>alert("This email id exists already!");open(\'http://127.0.0.1:5000/\', \'_self\');</script>'
	new_user = User(email=email, password=generate_password_hash(passw))
	db.session.add(new_user)
	db.session.commit()
	return redirect('/')


if __name__ == '__main__':
	app.run(debug=True)
