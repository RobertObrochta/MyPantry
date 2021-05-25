
from datetime import datetime
import copy

# a general log of meals and food items
saved_items = {}
saved_meals = {}

# a daily log of food items and nutrients gathered
items_eaten_today = {} # which item : how many of them
nutrients_eaten_today = {} # running total of the nutrients consumed for each day
                  
def insertItem(item, serving_size, macronutrients, additional_nutrients = None):
    'creates a new ingredient item'
    if type(macronutrients) != dict:
        print("Ensure that the macronutrients are stored as a dictionary.")
        return False
    # converts the macronutrients to floats instead of strings
    else:
        ingredient_details = [1, macronutrients, additional_nutrients]
        # scale serving_size to its base form of 1 serving
        for key, amount in macronutrients.items():
            if type(amount) == int or type(amount) == float:
                base_value = amount / serving_size
                macronutrients[key] = base_value
                saved_items[item.lower()] = ingredient_details

            elif "g" in amount:
                g_index = amount.find("g")
                # checks to see if it is a mg content or not
                mg_index = amount[g_index - 1]
                if mg_index.isdigit():
                    base_value = float(amount[0:g_index]) / serving_size
                    macronutrients[key] = base_value
                else: 
                    base_value = float(amount[0:g_index - 1]) / serving_size
                    macronutrients[key] = base_value
                saved_items[item.lower()] = ingredient_details

        return True


def createMeal(meal_name = "Custom Meal", ingredients = {}):
    'creates a meal using inserted ingredients'

    meal_ingrs = copy.deepcopy(saved_items)
    ingr_dict = {}
    for key, amount in ingredients.items():
        if key.lower() not in saved_items.keys():
            print(f"{key} is not in your past food items. Please register it before adding it to a meal.")
            return False
         
        ingredient_details = meal_ingrs.get(key)
        ingredient_details[0] = amount
        for k, macro in ingredient_details[1].items():
            updated_value = macro * amount
            ingredient_details[1][k] = updated_value
        
        # leave the addtnl_nutrients out of this for now
        ingr_dict[key] = ingredient_details

    saved_meals[meal_name] = ingr_dict
    # return meal_ingrs for use in logMeal
    return meal_ingrs


def logMeal(item, amount = 1):
    'keeps track of item/meal eaten throughout the day. Also keeps a running track of macros'
    # items will be kept as a dictionary, used in the graphing part of this project (separate file)
    total_calories = 0
    total_protein = 0
    total_fats = 0
    total_carbs = 0

    temp_dict = {}

    if item.lower() not in saved_items.keys() and item.lower() not in saved_meals.keys():
        print(f"{item} is not in your database. Register it before logging.")
        return False
    
    if item.lower() in saved_items.keys():
        # find the item that will be logged
        for key, details in saved_items.items():
            if key == item.lower():
                total = saved_items.get(key)
                total[0] = amount
                for k, macro in total[1].items():
                    updated_value = macro * amount
                    total[1][k] = updated_value
                temp_dict[item] = total

################################################## still need to finish this ###############################################################
    '''
    Now do the same thing, but for meals. Then, gather the information and keep a nutrient counter DICTIONARY
    format = {mdy : {"protein" : running_total, "carbs" : running total} }
    '''
############################################################################################################################################
    timestamp = datetime.now()
    dmy = timestamp.day, timestamp.month, timestamp.year

    items_eaten_today[dmy] = temp_dict
    return timestamp


def showDicts():
    print("Your past food items: ")
    for item in saved_items.keys():
        print(item)
    print("\n")

    print("Your meals: ")
    for item in saved_meals.keys():
        print(item + "\n")





'''
----------------------------------------------------------------------UI Elements below here--------------------------------------------------------------------------
'''
# UI element for logging existing meals
def logIM():
    while True:
        item = input("What did you eat today? ")
        howMuch = float(input(f"How much {item} did you eat today? "))
        logMeal(item, howMuch)
        print(items_eaten_today)
        return True

# UI element for logging new food items
'''
FORMAT ===== insertItem(item **str**, serving_size **int or float**, macronutrients **dict**, additional_nutrients = None **dict**):
'''
def addItem():
    while True:
        item = input("What do you want to add? ")
        serving_size = float(input(f"How much {item} did you eat today? "))
        macros = input("Add comma-separated macronutrients: ").split(",") 
        amount_macros = input("In the same order of your macronutrients, add the corresponding amount: ").split(",")
        # additional_nutrients = input("Add addtional nutrients with the format -- nutrient:amount. ")

        macros_dict = {}
        # add the macros
        for a, m in zip(amount_macros, macros):
            macros_dict[m] = float(a)

        insertItem(item, serving_size, macros_dict)
        print(f"Added {item} to your pantry!")
        return True


# UI element for logging new meals
'''
FORMAT ===== createMeal(meal_name = "Custom Meal", ingredients = {}):
'''
def addMeal():
    while True:
        meal_name = input("Enter a meal name: ")
        ingredient_name = input("Add comma-separated ingredients: ").split(",") 
        ingredient_amount = input("In the same order of your macronutrients, add the corresponding amount. ").split(",")
        # additional_nutrients = input("Add addtional nutrients with the format -- nutrient:amount. ")

        ingredient_dict = {}
        # add the ingredients
        for n, a in zip(ingredient_name, ingredient_amount):
            ingredient_dict[n.strip()] = float(a)

        createMeal(meal_name, ingredient_dict)
        print(f"Added {meal_name} to your pantry!")
        return True

def startUp():
    print("Welcome to your pantry!")

def menu():
    print("OPTIONS: Register Item (1), Create Meal (2), Log Item/Meal (3), View All Saved Items (4), Quit (5)")
    choice = int(input().strip())
    while choice >= 1 and choice <= 4:
        if choice == 1:
            addItem()
        elif choice == 2:
            addMeal()
        elif choice == 3:
            logIM()
        elif choice == 4:
            showDicts()
        break

    # recursive method to keep the menu showing
    if choice >= 1 and choice <= 4:
        menu()
    else:
        print("See you!")
        return False

def main():
    startUp()
    menu()

main()