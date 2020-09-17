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
    eventRecurring = True if 'recurring' in request.form else False
    newEvent = Event(eventDate,eventName, eventGuests, eventLocation, eventDesc, eventRecurring)
    add_new_event(newEvent)
    return render_template('index.html', title='Home', events=events)

@app.route('/remove-event', methods=['POST'])
def remove_event():
    eventName = request.form["eventname"]
    eventDate = request.form["eventdate"]
    for event in events:
        if eventName == event.name and eventDate == event.date:
            remove_event_from_list(event)
    return render_template('index.html', title='Home', events=events)