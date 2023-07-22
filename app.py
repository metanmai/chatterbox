from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():  # put application's code here
	return 'Home Page'


@app.route('/about')
def about_page():
	return 'About Page'


if __name__ == '__main__':
	app.run(debug=True)
	