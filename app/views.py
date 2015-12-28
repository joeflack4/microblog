from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    #return "Hello, World!"
	return render_template('index.html')
	
#@app.route('/hello/')
#@app.route('/hello/<name>')
#def hello(name=None):
#    return render_template('hello.html', name=name)