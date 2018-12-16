from flask import Flask
app = Flask(__name__)

@app.route('/')                 #index page
def index():
    return 'Index Page'

@app.route('/hello')            #test route
def hello():
    return 'Hello'