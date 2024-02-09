from flask import Flask, g, redirect, url_for, render_template, request

# Constructor, the path of the correct module 
app = Flask(__name__) # initial Object

@app.before_request
def set_global_variables(): # global variables for the website
	g.useraccess = '' # Initialize null

@app.route('/')
def home():
	return render_template('index.html') # Initialize page

@app.route('/login', methods=['POST', 'GET'])
def logidn():    
	if request.method == "POST": # method POST
		g.useraccess = request.form['iuser'] # value html input
		return redirect(url_for('profile', user = g.useraccess)) # redirect profile page
	else: # method GET
		return render_template('login.html')

@app.route('/profile/<user>')# Use the route() decorator to bind a function to a URL.
def profile(user):# pass user as input value
	return render_template("profile.html", profiles = user)

if __name__ == "__main__":
	app.run(debug=True)