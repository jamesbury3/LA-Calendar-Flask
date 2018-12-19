import time
import calendar
import Scheduler

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')                 #index page
def index():
    times = Scheduler.getSchedule()
    unassigned_times = Scheduler.getUnWorkedTimes()
    return render_template('index.html', title='Home', times=times, unassigned_times = unassigned_times)
