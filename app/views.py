from flask import render_template
from app import app

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
