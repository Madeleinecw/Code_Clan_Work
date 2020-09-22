class Album:

    def __init__(self, name, genre, artist, id = None):
        self.name = name
        self.genre = genre
        self.artist = artist
        self.id = id

    def __str__(self):
        return f'Name: {self.name}, Genre: {self.genre}, Artist: {self.artist}, ID: {self.id}'