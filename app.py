from flask import Flask, render_template

from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '3727eb8d6702e4578cfa82cbb5767f0c'

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
def about_page():
	return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
	app.run(debug=True)
