import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.customers = {"Rich Guest": Guest("Cher", 200, "Believe"),
                    "Poor Guest": Guest("Adele", 10, "Hello"),
                    "Late Guest": Guest("Prince", 50, "Purple Rain"),
                    "Hungry Guest": Guest("Meatloaf", 75, "Bat out of Hell"),
                    "Thirsty Guest": Guest("Kelis", 40, "Milkshake"),
                    "Young Guest": Guest("Lorde", 50, "Royals"),
                    "Dancing Guest": Guest("Rihanna", 50, "Umbrella"),
                    "Arty Guest": Guest("Gaga", 50, "Paparazzi"),
                    "Pop Guest": Guest("Madonna", 50, "Holiday")}

        self.room_1 = Room(15)
        self.songs = [Song("Cher", "Believe"), Song("Madonna", "Holiday")]
 


    def test_check_in__can_afford(self):
        self.room_1.check_in(self.customers["Rich Guest"])
        self.assertEqual(1, len(self.room_1.occupancy))

    def test_check_in__can_not_afford(self):
        self.room_1.check_in(self.customers["Poor Guest"])    
        self.assertEqual(0, len(self.room_1.occupancy))
    
    def test_check_in__already_occupied(self):
        self.room_1.occupancy = ["Madonna", "Cher", "Gaga", "Kelis", "Rihanna"]
        self.room_1.check_in(self.customers["Late Guest"])
        self.assertEqual(5, len(self.room_1.occupancy))

    # def test_check_out(self):
    #     self.room_1.check_in(self.customers["Pop Guest"])
    #     self.room_1.check_in(self.customers["Rich Guest"])
    #     self.room_1.check_in(self.customers["Arty Guest"])
    #     self.room_1.check_in(self.customers["Thirsty Guest"])
    #     self.room_1.check_in(self.customers["Dancing Guest"])
    #     self.room_1.check_out(self.customers["Rich Guest"])
    #     self.assertEqual([Guest("Madonna", 50, "Holiday"), Guest("Gaga", 50, "Paparazzi"), Guest("Kelis", 40, "Milkshake"), Guest("Rihanna", 50, "Umbrella")], self.room_1.occupancy)

    def test_load_song(self):
        self.room_1.load_song(self.songs[0])
        self.assertEqual(1, len(self.room_1.tracks))
    
    def test_fave_song(self):
        self.room_1.load_song(self.songs[0])
        self.assertEqual("Wooo!", self.room_1.fave_song(self.customers["Rich Guest"]))