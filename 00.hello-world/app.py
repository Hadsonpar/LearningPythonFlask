from flask import Flask

app = Flask(__name__)
@app.route('/')

def helloworld():
    return 'Hola mundo desde Python y Flask'

if __name__ == '__main__':
    app.run()