# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, num_1):
    shop["admin"]["total_cash"] += num_1
    return shop["admin"]["total_cash"]

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, num_1):
    shop["admin"]["pets_sold"] += num_1
    return shop["admin"]["pets_sold"]

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    pets_list = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets_list.append(pet)

    return pets_list

def find_pet_by_name(shop, name):
    return_pet = None

    for pet in shop["pets"]:
        if pet["name"] == name:
            return_pet = pet

    return return_pet

def remove_pet_by_name(shop, name):
    shop["pets"].remove(find_pet_by_name(shop, name))
        
def add_pet_to_stock(shop,new_pet):
    shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash
    return get_customer_cash(customer)

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True 
    elif customer["cash"] < pet["price"]:
        return False
    
def sell_pet_to_customer(shop, pet, customer):
    if not pet or not customer_can_afford_pet(customer, pet):
        return
        
    remove_customer_cash(customer, pet["price"])
    add_pet_to_customer(customer, pet)
    add_or_remove_cash(shop, pet["price"])  
    increase_pets_sold(shop, 1)
    