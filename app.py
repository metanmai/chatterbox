from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == '__main__':
	app.run(debug=True)
