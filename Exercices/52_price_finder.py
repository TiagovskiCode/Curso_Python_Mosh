# Exercise 52: Simple Price Finder
# Objective: Practice basic dictionary lookup using an if/else statement.

store_menu = {"apple": 1.50, "banana": 0.75, "orange": 1.20}

def get_price(menu_dict, item):
    if item in menu_dict:
        return menu_dict[item]
    else:
        return "Item not found"


print(get_price(store_menu, "apple"))
print(get_price(store_menu, "grape"))
