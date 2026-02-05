def check_ingredients(ingredients):
    checking = ingredients.lower()
    gluten = ["wheat", "flour", "barley", "rye", "oats", "triticale", "malt"]
    gluten_free = ["gluten free", "gluten-free"]
    if any(word in checking for word in gluten_free):
        print("This product contains gluten free alternatives - enjoy!")
    elif any(word in checking for word in gluten):
        print("This product contains gluten - stay away!")
    else:
        print("This product does not contain gluten - enjoy!")

check_ingredients("<<<Insert list of ingredients here as a string>>>")

# test cases
# check_ingredients("wheat")
# check_ingredients("gluten free flour")
# check_ingredients("cabbage")