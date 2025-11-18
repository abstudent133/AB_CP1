#AB 1st Flexible calculator

#set up functions

#definition addition(*numbers)
    #total is sum(numbers)
    #return the total

#definition average(*numbers)
    #total is 0
    #for num in numbers
        #add num to total
    #answer is total divided by length of numbers
    #return answer

#definition maximun(*numbers)
    #maxi is max(numbers)
    #return maxi

#definition minimum(*numbers)
    #mini is min(numbers)
    #return mini

#definition get_numbers()
    #while true
        #numbers is [empty list]
        #if ask is integer or float
            #ask is ask them to input a number
            #numbers.append(ask)
        #elif ask is done
            #return numbers
            #break


#definition main(operation,*numbers)

    #if operation is sum
        #addition(numbers)
