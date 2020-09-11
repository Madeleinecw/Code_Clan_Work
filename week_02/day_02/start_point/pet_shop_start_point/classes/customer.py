# Customer - name, cash, pets[] (starts empty). add_remove_pet, add_remove_cash

class Customer:

    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.pets = []

    def pet_count(self):
       return len(self.pets)

    def add_pet(self, new_pet):
        self.pets.append(new_pet)

    def get_total_value_of_pets(self):
        total = 0
        for pet in self.pets:
            total += pet.price
        return total