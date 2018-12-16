from flask import Flask
app = Flask(__name__)

@app.route('/')                 #index page
def index():
    return 'Index Page'

class LA:
  def __init__(self, name, hours):
    self.name = name
    self.hours = hours
    self.worked = 0


@app.route('/hello')            #test route
def hello():
    p1 = LA("James", 10)
    return p1.name


