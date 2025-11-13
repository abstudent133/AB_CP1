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
    'side dishes':{
        'side dish 1'
    }
}
#definition check(ordering)
def check(ordering):
    #if ordering in key
    if ordering in menu[key].keys():
        #return true
        return True
    #else
    else:
        #reuturn false
        return False

#definition take order(ordering, key)
def take_order(ordering, key, order):
    #if check(ordering) is true
    if check(ordering) == True:
        #order [key] = ordering
       order[key] = ordering
    return order
#definition get price(ordering, key)
def price(ordering, key):
    #price is menu [key][ordering]
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
        ordering = input("What drink would you like:")
    #elif key is main course
    elif key == 'main course':
        #ordering is ask which main course they want
        ordering = input("Which main course would you like: ")
    #elif key is side dish 1
    elif key == 'side dish 1':
        #ording is ask which side dish they want first
        ordering = input("What would you like for your first side dish: ")
    #elif key is side dish 2
    elif key == 'side dish 2':
        #ordering is ask which side dish they want second
        ordering = input("What would you like for your second side dish: ")
    #call take order(ordering, key)
    order = take_order(ordering, key, order)
#for key in order
for key in order.keys():
    total = 0
    #total += price
    total += price(ordering, key)
#print keys
print(order['drink'])
print(order['main course'])
print(order['side dish 1'])
print(order['side dish 2'])
#show total
print(total)

