customers = [
            {
                "name": "Alice",
                "pets": [],
                "cash": 1000
            },
            {
                "name": "Bob",
                "pets": [],
                "cash": 50
            },
            {
                "name": "Jack",
                "pets": [],
                "cash": 100
            }
        ]



pet_shop = {
            "pets": [
                {
                    "name": "Sir Percy",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "King Bagdemagus",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "Sir Lancelot",
                    "pet_type": "dog",
                    "breed": "Pomsky",
                    "price": 1000,
                },
                {
                    "name": "Arthur",
                    "pet_type": "dog",
                    "breed": "Husky",
                    "price": 900,
                },
                {
                    "name": "Tristan",
                    "pet_type": "cat",
                    "breed": "Basset Hound",
                    "price": 800,
                },
                {
                    "name": "Merlin",
                    "pet_type": "cat",
                    "breed": "Egyptian Mau",
                    "price": 1500,
                }
            ],
            "admin": {
                "total_cash": 1000,
                "pets_sold": 0,
            },
            "name": "Camelot of Pets"
        }
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

# # Test 16
def get_customer_pet_count(customer):
    return len(customer["pets"])

# # Test 17
def  add_pet_to_customer(customer, new_pet):
    customer["pets"].append([new_pet])
    return len(customer["pets"])

# Test 18 & 19
def customer_can_afford_pet(customer,pet):
    if customer["cash"] >= pet["price"]:
        return True
    else: 
        return False

# Test 20 & 21 & 22
def sell_pet_to_customer(pet_shop,pet,customer):
    num_sold = 1
    cost = pet["price"]
    if pet in pet_shop["pets"] and customer_can_afford_pet(customer,pet) == True:
        add_pet_to_customer(customer,pet)
        increase_pets_sold (pet_shop, num_sold)
        remove_customer_cash(customer,cost)
        add_or_remove_cash(pet_shop,cost)
        return get_customer_cash(customer), get_total_cash(pet_shop), get_pets_sold(pet_shop)
customer = customers[0]
pet = find_pet_by_name(pet_shop,"Arthur") 
print (sell_pet_to_customer(pet_shop,pet,customer))