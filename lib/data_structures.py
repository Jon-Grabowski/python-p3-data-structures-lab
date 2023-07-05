spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(food['name']+' ('+food["cuisine"]+') | Heat Level: '+(food['heat_level'] * "🌶"))
        
    # [print(food['name']+' ('+food["cuisine"]+') | Heat Level: '(food['heat_level'] * "🌶")) for food in spicy_foods]


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'].lower() == cuisine.lower():
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(food['name']+' ('+food["cuisine"]+') | Heat Level: '+(food['heat_level'] * "🌶"))

def get_average_heat_level(spicy_foods):
    heat_total = 0
    for food in spicy_foods:
        heat_total += food['heat_level']
    return heat_total / len(spicy_foods)
    

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods+[spicy_food]

