from flask import Flask # import to initialize

# Constructor, the path of the correct module 
app = Flask(__name__) # initial Object
@app.route('/')

def helloworld():
    return 'Debug project Python y Flask'

# Modified program for see debug incorport Werkzeug
@app.route('/<message>')
def fmessage(message):    
    return f'Your message ir {int(message)}'

if __name__ == '__main__':
    app.run(debug=True) # debug project