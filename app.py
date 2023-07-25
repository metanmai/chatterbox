import datetime

from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '3727eb8d6702e4578cfa82cbb5767f0c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	
	# Inside db.relationship, Post has a capital P because we are directly referring to the class.
	posts = db.relationship('Post', backref='author', lazy=True)
	
	def __repr__(self):
		return f'User{self.username}, {self.image_file}, {self.email}'


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
	content = db.Column(db.Text, nullable=False)
	
	# Inside db.ForeignKey, user is in lowercase because user is the name of the table.
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	def __repr__(self):
		return f'Post{self.title}, {self.date_posted}'
	

posts = [
	{
		'author': 'Tanmai Niranjan',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'April 20th, 2018'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'June 23rd, 2023'
	}
]


@app.route('/')
@app.route('/home')
def home():  # put application's code here
	return render_template('home.html', posts=posts)


@app.route('/about')
def about():
	return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for { form.username.data }!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	
	if form.email.data == 'admin@chatterbox.com' and form.password.data == 'password':
		flash('Logged in successfully.', 'success')
		return redirect(url_for('home'))
	
	else:
		flash('Login Unsuccessful, Please try again.', 'danger')
	
	return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
	app.run(debug=True)
