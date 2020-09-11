class PetShop:
    def __init__(self, name, pets, total_cash):
        self.name = name
        self.pets = pets
        self.total_cash = total_cash
        self.pets_sold = 0

    
    def stock_count(self):
        return len(self.pets)

    def increase_pets_sold(self):
        self.pets_sold += 1
    
    def increase_total_cash(self, new_cash):
        self.total_cash += new_cash 

    def add_pet(self, new_pet):
        self.pets.append(new_pet)

    def remove_pet(self, pet_name):
           self.pets.remove(pet_name)

    def find_pet_by_name(self, pet_name):
        for pet in self.pets:
            if pet.name == pet_name:
                return pet

    def sell_pet_to_customer(self, pet_name, customer):
        pet = self.find_pet_by_name(pet_name)
        customer.add_pet(pet)
        self.increase_pets_sold()
        self.remove_pet(pet)
        self.increase_total_cash(pet.price)


