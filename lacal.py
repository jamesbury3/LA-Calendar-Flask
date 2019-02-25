import time
import Scheduler
import collections
from forms import SearchForm

from flask import Flask, redirect, url_for
from flask import render_template
app = Flask(__name__)
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET','POST'])                 #index page
def index():

    form = SearchForm()
    current_name = ""
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

    on_day = [False, False, False, False, False]

    unassigned_times = Scheduler.getUnWorkedTimes()         #gets the unassigned times
    if form.validate_on_submit():
        current_name = form.la_name.data
        for time in monday:
            if current_name in monday.get(time):
                on_day[0] = True
        for time in tuesday:
            if current_name in tuesday.get(time):
                on_day[1] = True
        for time in wednesday:
            if current_name in wednesday.get(time):
                on_day[2] = True
        for time in thursday:
            if current_name in thursday.get(time):
                on_day[3] = True
        for time in friday:
            if current_name in friday.get(time):
                on_day[4] = True
        return render_template('index.html', title='Home', times=times, unassigned_times = unassigned_times, \
    monday = monday, tuesday = tuesday, wednesday = wednesday, thursday = thursday, friday = friday, form = form, name = current_name, \
    on_day = on_day)
    
    on_day = [True, True, True, True, True]
    return render_template('index.html', title='Home', times=times, unassigned_times = unassigned_times, \
    monday = monday, tuesday = tuesday, wednesday = wednesday, thursday = thursday, friday = friday, form = form, name = current_name, \
    on_day = on_day)