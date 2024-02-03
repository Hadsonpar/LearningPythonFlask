from flask import Flask # import to initialize
from markupsafe import escape # import markupsafe and apply escape

# Constructor, the path of the correct module 
app = Flask(__name__) # initial Object
@app.route('/')

@app.route('/<message>')
def fmessage(message):    
    return f'Your message ir: {escape(message)}'

if __name__ == '__main__':
    app.run(debug=True) # debug project