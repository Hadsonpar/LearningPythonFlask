from flask import Flask # import to initialize

# Constructor, the path of the correct module 
app = Flask(__name__) # initial Object
@app.route('/')

def helloworld():
    #return 'Hola mundo desde Python y Flask'
    return 'Debug project Python y Flask'

if __name__ == '__main__':
    app.run(debug=True) # debug project