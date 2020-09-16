from room import Room
from guest import Guest

room_1 = Room(25)
customer = Guest("Cher", 70, "Believe")

room_1.check_in(customer)
print(room_1.check_total_tab())