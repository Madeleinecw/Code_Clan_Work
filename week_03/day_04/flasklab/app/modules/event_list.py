from app.modules.event import *

event1 = Event('02/04/21', 'Convention', 30, '1st Floor', 'Comics Convention', True)
event2 = Event('11/04/21', 'Irn Blues', 45, 'Ground Floor', 'Scottish Blues Dancing Festival', False)

events = [event1, event2]

def add_new_event(event):
    events.append(event)

def remove_event_from_list(event):
    events.remove(event)