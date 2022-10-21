# WRITE YOUR FUNCTIONS HERE
# Test 1
def get_pet_shop_name (pet_shop):
    name = pet_shop ["name"]
    return name

# Test 2
def get_total_cash(pet_shop):
    total = pet_shop ["admin"]["total_cash"]
    return total

# Test 3 & 4
def add_or_remove_cash(pet_shop,add):
    pet_shop["admin"]["total_cash"]+= add
    return  get_total_cash

# Test 5 
def get_pets_sold(pet_shop):
    pets_sold = pet_shop["admin"]["pets_sold"]
    return pets_sold

# Test 6 
def increase_pets_sold (pet_shop, num_sold):
    pet_shop["admin"]["pets_sold"]+= num_sold
    return get_pets_sold

#  Test 7 
def get_stock_count(pet_shop):
    stock = len(pet_shop["pets"])
    return stock

# Test 8 
def get_pets_by_breed (pet_shop,breed):
    pets_by_breed = [ ]
    for pet in pet_shop["pets"][0]:
        if pet_shop["pets"][0]["breed"]== breed:
            pets_by_breed += pet_shop["pets"][0]["breed"]
    return pets_by_breed
