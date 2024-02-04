from flask import Flask # import to initialize
from markupsafe import escape # import markupsafe and apply escape

# Constructor, the path of the correct module 
app = Flask(__name__) # initial Object
@app.route('/')

def helloworld():
    return 'Hola mundo desde Python y Flask'

# Routing add variables ruler
# variable "section" for including in the web page sections
@app.route('/home/<section>') # Use the route() decorator to bind a function to a URL.
def home(section):
    varf = sections(escape(section))
    return f'Title the section is: {varf}'

# Function for title return of the section
def sections(section):
    title_html = ''
    if (section == 'home'):
        title_html = "Review scalables solutiones."
    if (section == 'welcome'):
        title_html = "Maximize your business productivity."
    if (section == 'solutions'):
        title_html = "Personalized solutions."
    if (section == 'services'):
        title_html = "Our services."
    return title_html


if __name__ == '__main__':
    app.run(debug=True) # debug project