from flask import Flask # import to initialize

# Constructor, the path of the correct module 
app = Flask(__name__) # initial Object

# Simulate pages load of a website, applied unique url
@app.route('/') # start unique url home
def home():
    varf = page_content('home')
    return f'Page - Home: {varf}'

@app.route('/about')
def about():
    varf = page_content('about')
    return f'Page - About: {varf}'

@app.route('/services')
def service():
    varf = page_content('services')
    return f'Page - Services: {varf}'

def page_content(page):
    title_html = ''
    if (page == 'home'):
        title_html = "Welcome a Flask Framework."
    if (page == 'about'):
        title_html = "Learning Python and Flask Framework."
    if (page == 'services'):
        title_html = "<br>- Learning<br>- Tutorials<br>- Projects"# br is html, combining python code and html
    return title_html

if __name__ == '__main__':
    app.run(debug=True) # debug project