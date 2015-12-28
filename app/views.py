from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/index/<name>')
def index(name=None):
    #How to use in local environment: 
	#	localhost:5000/index/name
	
	return render_template('index.html', name=name)