from flask import Flask, g, redirect, url_for, render_template, request

# Constructor, the path of the correct module 
app = Flask(__name__) # initial Object

@app.before_request
def set_global_variables(): # global variables for the website
	g.useraccess = 'hadson' # default user
	g.userpassw = '1234' # default password

@app.route('/')
def home():
	return render_template('index.html') # Initialize page

@app.route('/login', methods=['POST', 'GET'])
def logidn():
	error = '' # none variable for error capture
	if request.method == "POST": # method POST
		# validating credential
		if (request.form['iuser'] == g.useraccess and request.form['ipass'] == g.userpassw):
			# values html input, request
			return redirect(url_for('profile', user = request.form['iuser'])) # redirect profile page
		else: # your credential incorrect
			error = 'Invalid username/password'

	# else return method GET
	return render_template('login.html', page='Login', error=error)

@app.route('/profile/<user>')# Use the route() decorator to bind a function to a URL.
def profile(user):# pass user as input value
	return render_template("profile.html", profiles = user)

@app.route("/logout")
def logout():
    return redirect(url_for("login"))

if __name__ == "__main__":
	app.run(debug=True)