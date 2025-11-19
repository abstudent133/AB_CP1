#AB 1st Flexible calculator

#set up functions

#definition addition(*numbers)
def addition(*numbers):
    #total is sum(numbers)
    total = sum(numbers)
    #return the total
    return total

#definition average(*numbers)
def average(*numbers):
    #total is 0
    total = 0
    #for num in numbers
    for num in numbers:
        #add num to total
        total += total
    #answer is total divided by length of numbers
    answer = total/len(numbers)
    #return answer
    return answer

#definition maximun(*numbers)
def maximum(*numbers):
    #maxi is max(numbers)
    maxi = max(numbers)
    #return maxi
    return maxi

#definition minimum(*numbers)
def minimum(*numbers):
    #mini is min(numbers)
    mini = min(numbers)
    #return mini
    return mini

#definition get_numbers()
def get_numbers():
    #numbers is empty list
    numbers = []
    #while true
    while True:
        #number is ask for number
        number = input("Number: ")
        #if number is integer or float:
        if number.isnumeric():

            #contiue
        #elif number is done
            #break
    #return numbers

#definition main(operation,*numbers)
    #if operation is sum
        #add = addition(numbers)
        #return f"Calculate average of: {numbers}""
        #return f"Result: {add}"
    #elif operation is average
        #aver = average(numbers)
        #return f"Calculate average of: {numbers}""
        #return f"Result: {aver}"
    #elif operation is maximum
        #max = maximum(numbers)
        #return f"Calculate average of: {numbers}""
        #return f"Result: {max}"
    #elif operation is miniumum
        #min = minimum(numbers)
        #return f"Calculate average of: {numbers}""
        #return f"Result: {min}"
    #else
        #say invalid operation

#give instructions
#while true
    #operation is ask what they would like to do
    #numbers is get_numbers()
    #print main(operation, numbers)
    #action = ask if would like to continue
    #if action is yes
        #contiue
    #else
        #break
#show thank you for using the flexible calculator


