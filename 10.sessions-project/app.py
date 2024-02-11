from flask import Flask, g, redirect, url_for, render_template, request, session # initialize flask, global variables, redirect, url_for, render_template, request and session
from datetime import timedelta # import datetime for session time control

# Constructor, the path of the correct module 
app = Flask(__name__) # initial Object
app.secret_key = 'test' # storeding in secret_key a cryptographically-signed 
app.permanent_session_lifetime = timedelta(seconds=20) # session time control for 1 minute or 20 seconds as test

@app.before_request
def set_global_variables(): # global variables for the website
	g.useraccess = 'hadson' # default user
	g.userpassw = '1234' # default password

@app.route('/')
def home():
	return render_template('index.html') # Initialize page

@app.route('/login', methods=['POST', 'GET'])
def logidn():
	error = '' # empty variable for error capture
	if request.method == "POST": # method POST		
		# validating credential
		if (request.form['iuser'] == g.useraccess and request.form['ipass'] == g.userpassw):    		
			session.permanent = True			
			user = request.form['iuser'] # values html input, request
			session['user'] = user # session user start
			return redirect(url_for('profile')) # redirect profile page
		else: # your credential incorrect
			error = 'Invalid username/password'

	# else return method GET
	return render_template('login.html', page='Login', error=error)

@app.route('/profile')# Use the route() decorator to bind a function to a URL.
def profile():# pass user as input value
	if 'user' in session:
		user = session['user'] # session user capture
		return render_template("profile.html", profiles=user)
	else:
		return redirect(url_for("login")) # redirect fuction login (login page)
	
@app.route("/logout")
def logout():    
    session.pop('user', None)# session user clear
    return redirect(url_for("login")) # redirect fuction login (login page)
	
if __name__ == "__main__":
	app.run(debug=True)