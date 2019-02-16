import time
import Scheduler
import collections

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
#bootstrap = Bootstrap(app)

@app.route('/')                 #index page
def index():
    times = Scheduler.getTimesAndLAs()                      #gets the dictionary of times and las at each time
    monday = collections.OrderedDict()
    tuesday = collections.OrderedDict()
    wednesday = collections.OrderedDict()
    thursday = collections.OrderedDict()
    friday = collections.OrderedDict()

    for time in times:                                      #creates a new dictionary for each day of the week
        if 'Monday' in time:
            monday[time] = times.get(time)
        if 'Tues' in time:
            tuesday[time] = times.get(time)
        if 'Wed' in time:
            wednesday[time] = times.get(time)
        if 'Thur' in time:
            thursday[time] = times.get(time)
        if 'Fri' in time:
            friday[time] = times.get(time)

    unassigned_times = Scheduler.getUnWorkedTimes()         #gets the unassigned times
    return render_template('index.html', title='Home', times=times, unassigned_times = unassigned_times, \
    monday = monday, tuesday = tuesday, wednesday = wednesday, thursday = thursday, friday = friday, site = "index")

@app.route('/swap_shifts')
def swap_shifts():
    return render_template('swap_shifts.html', site = "swap")
