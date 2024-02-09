from flask import Flask, render_template # import to initialize

# Constructor, the path of the correct module cd
app = Flask(__name__) # initial Object

@app.route('/') 
def index():
    return render_template('Index.html', page='Index')

@app.route('/home')
def home():
    varf = page_content('home')
    return render_template('home.html', page='Home', content=varf)

@app.route('/about')
def about():
    varf = page_content('about')
    return render_template('about.html', page='About', content=varf)

@app.route('/services')
def service():
    varf = page_content('services')
    return render_template('services.html', page='Services', content=varf)

@app.route('/projects')
def projects():
    varf = page_content('projects')
    return render_template('projects.html', page='Projects', content=varf)

@app.route('/contact')
def contact():
    varf = page_content('contact')
    return render_template('contact.html', page='Contact Us', content=varf)

def page_content(page):
    title_html = ''
    if (page == 'home'):
        title_html = "Welcome a Flask Framework."
    if (page == 'about'):
        title_html = "Learning Python and Flask Framework."
    if (page == 'services'):
        title_html = "Our Services."
    if (page == 'projects'):
        title_html = "Our Projects."    
    if (page == 'contact'):
        title_html = "Contact Us"    
    return title_html

if __name__ == '__main__':
    app.run(debug=True) # debug project