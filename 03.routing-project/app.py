from flask import Flask # import to initialize

# Constructor, the path of the correct module 
app = Flask(__name__) # initial Object
@app.route('/')

def helloworld():
    return 'Hola mundo desde Python y Flask'

# Routing: Applied for modern web applications use meaningful URLs to help users
@app.route('/home') # Use the route() decorator to bind a function to a URL.
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True) # debug project