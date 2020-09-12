import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song 

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.customers = {"Rich Guest": Guest("Cher", 200, "Believe"),
                    "Poor Guest": Guest("Adele", 10, "Hello"),
                    "Late Guest": Guest("Prince", 50, "Purple Rain"),
                    "Hungry Guest": Guest("Meatloaf", 75, "Bat out of Hell")}

        self.room_1 = Room(15)
        self.songs = [Song("Cher", "Believe"), Song("Madonna", "Holiday")]

        
        
