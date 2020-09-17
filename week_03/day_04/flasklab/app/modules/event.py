class Event:

    def __init__(self, date, name, number_of_guests, room_location, description, recurring):
        self.name = name 
        self.date = date 
        self.number_of_guests = number_of_guests
        self.description = description
        self.room_location = room_location
        self.recurring = recurring

        