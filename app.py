import time
import calendar

from flask import Flask
app = Flask(__name__)

@app.route('/')                 #index page
def index():
    return 'Index Page'

@app.route('/hello')            #test route
def hello():
    p1 = LA("James", 10)
    return p1.name


