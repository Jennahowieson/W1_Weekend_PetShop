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
def find_pet_by_name(pet_shop,pet_name):
    for pet in pet_shop["pets"]:
        if pet_name == (pet["name"]):
            return pet

print(len(find_pet_by_name(pet_shop,"Arthur")))
print(find_pet_by_name(pet_shop,"Arthur"))

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop ["pets"]:
        if pet_name == (pet["name"]):
            del pet

pet = find_pet_by_name(pet_shop,"Arthur")
print (remove_pet_by_name(pet_shop, "Arthur"))
print(find_pet_by_name(pet_shop,"Arthur"))