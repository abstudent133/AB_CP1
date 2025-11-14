#AB 1st Order Up!
#make menu dictionary
menu = {
    #drinks dictionary
    "drink":{
        'milk shake':3,
        'iced tea':2,
        'orange juice':4,
        'coffee':5
    },

    #main course dictionary
    'main course':{
        'cheeseburger':34,
        'cheese sandwich':22,
        'chicken burgers':23,
        'spicy chicken':33,
        'hot dog':24
    },

    #side dishes dictionary
    'side dishes':{
        'fruit salad':13,
        'nuggets':14,
        'french fries':15,
        'corn on the cob':14
    }
}

#make order dictionary
order = {
    #drink
    'drink':"",
    #main course
    'main course':"",
    #side dish 1
    'side dish 1':"",
    #side dish 2
    'side dish 2':""
}

#definition check(ordering, key)
def check(ordering, key):
    #if ordering in key
    # (fixed so side dish 1 and 2 check "side dishes")
    if key in ["drink", "main course"]:
        return ordering in menu[key].keys()

    if key in ["side dish 1", "side dish 2"]:
        return ordering in menu["side dishes"].keys()

    #else
    else:
        #return false
        return False


#definition take order(ordering, key, order)
def take_order(ordering, key, order):
    #if check(ordering) is true
    if check(ordering, key) == True:
        #order[key] = ordering
        order[key] = ordering
    return order


#definition get price(ordering, key)
def price(ordering, key):
    #price is menu[key][ordering]
    prices = menu[key][ordering]
    #return price
    return prices


#print the menu
print(f"These are your drink options: {menu['drink']}")
print(f"These are your main course options: {menu['main course']}")
print(f"These are your side dish options: {menu['side dishes']}")

#for key in order
for key in order.keys():

    # if key is drink
    if key == 'drink':
        #ordering is ask which drink they want
        ordering = input("What drink would you like: ").lower()

    #elif key is main course
    elif key == 'main course':
        #ordering is ask which main course they want
        ordering = input("Which main course would you like: ").lower()

    #elif key is side dish 1
    elif key == 'side dish 1':
        #ordering is ask which side dish they want first
        ordering = input("What would you like for your first side dish: ").lower()

    #elif key is side dish 2
    elif key == 'side dish 2':
        #ordering is ask which side dish they want second
        ordering = input("What would you like for your second side dish: ").lower()

    #call take order(ordering, key)
    take_order(ordering, key, order)


#calculate total
total = 0

#for key in order
for key in order.keys():

    # find correct menu category
    # (side dish 1 & 2 both use "side dishes")
    if key in ["side dish 1", "side dish 2"]:
        menu_key = "side dishes"
    else:
        menu_key = key

    #total += price
    total += price(order[key], menu_key)


#print keys
print(order['drink'])
print(order['main course'])
print(order['side dish 1'])
print(order['side dish 2'])

#show total
print(f"This is your total: ${total}")

