class Room:

    def __init__(self, entry):
        self.entry = entry
        self.capacity = 5
        self.occupancy = []
        self.tab = 0
        self.tracks = []
        self.bar = []

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

    def add_stock_to_bar(self, refreshment):
        self.bar.append(refreshment)

    # Not really how bars work but ok 
    def check_total_tab(self):
        guest_funds = 0
        available_credit = 0
        for guest in self.occupancy:
            guest_funds += guest.wallet
        if guest_funds > self.tab:
            available_credit = guest_funds - self.tab
        return available_credit
    
    def serve_guest_refreshment(self, refreshment):
        if self.check_total_tab() <= refreshment.price:    
            self.tab += refreshment.price
            refreshment.stock -= 1
            
    