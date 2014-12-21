from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	#return 'Hello, World!'
	user = {'nickname':'Migul'} #fake user
	posts = [# fake array of posts
		{
			'author':{'nickname': 'John'},
			'body': 'Beautiful day in Portland!'
		},
		{
			'author': {'nickname': 'Susan'},
			'body': 'The Avengers movie was so cool!'
		}
	]
	return render_template("index.html",
		title = "Home",
		user = user,
		posts = posts)
 
    # return '''

    # <html>
    # <head>
	#   <title>Home Page</title>
	# </heaad>
	#<body>
	#   <h1>Hello, ''' + user['nickname'] + '''</h1>
	# </body>
    # </html>
@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html',
		title = 'Sign In',
		form = form)
