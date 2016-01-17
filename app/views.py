from flask import render_template, url_for
from app import app

@app.route('/')
#@app.route('/index')
#@app.route('/index/<name>')
def index():
    #How to use in local environment: 
	#	localhost:5000/index/name
	
	return render_template('/AdminLTE/index.html')