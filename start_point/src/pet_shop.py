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

# Test 8 & 9
def get_pets_by_breed(pet_shop,breed):
    pets_by_breed = []
    for pet in pet_shop["pets"]:
        if breed == (pet["breed"]):
            pets_by_breed.append(pet["name"])
    return pets_by_breed

# Test 10 & 11
def find_pet_by_name(pet_shop,pet_name):
    for pet in pet_shop["pets"]:
        if pet_name == (pet["name"]):
            return pet
        
# Test 12
def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet_name == (pet["name"]):
            pet_shop["pets"].remove(pet)

# Test 13
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append([new_pet])

# Test 14
def get_customer_cash(customer):
    return customer["cash"]

# Test 15
def remove_customer_cash(customer,spend):
    customer["cash"]-= spend
    return customer

# Test 16
def get_customer_pet_count(customer):
    return len(customer["pets"])

# Test 17
def  add_pet_to_customer(customer, new_pet):
    customer["pets"].append([new_pet])
    return len(customer["pets"])

# Test 18
