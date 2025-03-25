# lab15.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# from templates import my_template_1

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)
# route decorator binds a function to a URL
@app.route('/')
def hello():
    return f"<h1>Acronyms</h1> <h1>Oscar: NBA</h1>"
@app.route('/jaime')
def t_test():
    return render_template('my_template_1.html')
