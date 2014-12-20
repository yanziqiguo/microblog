from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	#return 'Hello, World!'
	user = {'nickname':'Migul'} #fake user
	return render_template("index.html",
		title = "Home",
		user = user)
 
    # return '''

    # <html>
    # <head>
	#   <title>Home Page</title>
	# </heaad>
	#<body>
	#   <h1>Hello, ''' + user['nickname'] + '''</h1>
	# </body>
    # </html>
