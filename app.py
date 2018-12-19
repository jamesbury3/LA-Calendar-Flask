import time
import calendar
import Scheduler

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')                 #index page
def index():
    user = Scheduler.getSchedule()
    return render_template('index.html', title='Home', user=user)




