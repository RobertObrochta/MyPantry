
# this dictionary will eventually be stored in a database, but for the purposes of visualizing and getting set up, store in the dictionary
saved_items = {}
                        # macronutrients HAS to be a dictionary with the name of macro : amount of macro. Same with additional_nutrients
# this function will take a serving_size of a food and reduce it down to its base form (1g, or 1oz). Therefore, will change all of the contents and scale them accordingly
def insertFood(food, serving_size, macronutrients, additional_nutrients = None):
    saved_items[food] = [macronutrients, serving_size, additional_nutrients]

food = "pizza"
macro = {"protein": "15g", "carbohydrates": '12g'}
serving_size = 1

food2 = "burger"
macro2 = {"protein": "20g", "carbohydrates": '1g'}
serving_size2 = 2

insertFood(food, serving_size, macro)
insertFood(food2, serving_size2, macro2)
print(saved_items)