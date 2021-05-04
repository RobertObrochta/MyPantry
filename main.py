
# these dictionaries will eventually be stored in a database, but for the purposes of visualizing and getting set up, store in the dictionary
saved_items = {}
saved_meals = {}
                  
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



def createMeal(mealName = "Custom Meal", ingredients = {}):
    'create a meal using inserted ingredients'

    ingr_dict = {}
    for key, amount in ingredients.items():
        if key not in saved_items.keys():
            print(f"{key} is not in your past food items. Please register it before adding it to a meal.")
            return False
        
        ingredient_details = saved_items.get(key)
        ingredient_details[0] = amount
        for k, macro in ingredient_details[1].items():
            updated_value = macro * amount
            ingredient_details[1][k] = updated_value
        
        # leave the addtnl_nutrients out of this for now
        ingr_dict[key] = ingredient_details

    saved_meals[mealName] = ingr_dict
    return saved_meals

# function to show total macros and additional nutrients of a meal COMING NEXT
    


def showDicts():
    print("Your past food items: ")
    for item in saved_items.keys():
        print(item)
    print("\n")

    print("Your meals: ")
    for item in saved_meals.keys():
        print(item)



# SAMPLE INPUTS BELOW
# food = "pizza"
# macro = {"fat" : "2g","protein" : 15, "carbohydrates" : '12g'}
# serving_size = 1

# food2 = "burger"
# macro2 = {"protein" : "20g", "carbohydrates" : '1g', "sodium" : "125mg"}
# serving_size2 = 2

# insertItem(food, serving_size, macro)
# insertItem(food2, serving_size2, macro2)

# createMeal("cheese", {"burger": 2, "pizza": 3})
