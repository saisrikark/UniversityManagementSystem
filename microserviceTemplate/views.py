from myapp import app
from models import *
from flask import render_template

@app.route('/')
def index():
    #return "</h1>Hello World</h1>"
    return render_template('loginPage.html')

@app.route('/loginSubmission', methods=['POST'])
def loginSubmission():
    pass
