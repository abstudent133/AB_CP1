#AB 1st Order Up!
#make menu dictionary
    #drinks dictionary
    #main course dictionary
    #side dishes dictionary

#make order dictionary
    #drink
    #main course
    #side dish 1
    #side dish 2
#definition check(ordering)
    #if ordering in key
        #return true
    #else
        #reuturn false

#definition take order(ordering, key)
    #call check(ordering)
    #if check(ordering) is true
        #order [key] = ordering
        #return ordering
#definition get price(ordering, key)
    #price is menu [key][ordering]
    #return price

#print the menu

#for key in order
    # if key is drink
        #ordering is ask which drink they want
    #elif key is main course
        #ordering is ask which main course they want
    #elif key is side dish 1
        #ording is ask which side dish they want first
    #elif key is side dish 2
        #ordering is ask which side dish they want second
    #call take order(ordering, key)
#for key in order
    #price is get price(ordering, key)
    #total += price
#for key in order
    #print key
#show total

