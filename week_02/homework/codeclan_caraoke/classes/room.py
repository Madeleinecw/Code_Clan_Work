class Room:

    def __init__(self, entry):
        self.entry = 15
        self.capacity = 5
        self.occupancy = []
        self.tab = []
        self.tracks = []

    def check_in(self, guest):
        if guest.wallet >= self.entry and self.capacity > len(self.occupancy):
            guest.wallet -= self.entry
            self.occupancy.append(guest)

    def check_out(self, guest):
        self.occupancy.remove(guest)

    def load_song(self, song):
        self.tracks.append(song)

    def fave_song(self, guest):
        for song in self.tracks:
           if song.title == guest.favourite_song:
               return "Wooo!"
