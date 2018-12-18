import time
import calendar

from flask import Flask
app = Flask(__name__)

@app.route('/')                 #index page
def index():
    return 'Index Page'

class LA:                       #creates LA Class with a name, hours which should be a list of shift objects
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours
        self.worked = 0

class Shift:                    #creates shift class with a time slot which should be a time object and a list of LA's
    def __init__(self, time_slot, workers):
        self.workers = workers


@app.route('/hello')            #test route
def hello():
    p1 = LA("James", 10)
    return p1.name


