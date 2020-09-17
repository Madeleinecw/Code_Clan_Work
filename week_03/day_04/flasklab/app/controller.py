from app import app
from flask import render_template, request
from app.modules.event import *
from app.modules.event_list import *

@app.route('/')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/add-event', methods=['POST'])
def add_event():
    eventName = request.form["name"]
    eventDesc = request.form['description']
    eventDate = request.form['date']
    eventGuests = request.form['guests']
    eventLocation = request.form['location']
    eventRecurring = request.form['recurring']
    newEvent = Event(eventDate,eventName, eventGuests, eventLocation, eventDesc, eventRecurring)
    add_new_event(newEvent)
    return render_template('index.html', title='Home', events=events)

