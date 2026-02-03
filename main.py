def check_ingredients(ingredients):
    checking = ingredients.lower()
    gluten = ["wheat", "flour", "barley", "rye", "oats", "triticale", "malt"]
    if any(word in checking for word in gluten):
        print("This product contains gluten - stay away!")
    else:
        print("This product does not contain gluten - enjoy!")

check_ingredients("Insert list of ingredients as a string")