#AB 1st Flexible calculator

#set up functions

#definition addition(*numbers)
def addition(*numbers):
    #total is sum(numbers)
    total = 0
    #for num in numbers
    for num in numbers:
        total += num
    #return the total
    return total

#definition average(*numbers)
def average(*numbers):
    #total is 0
    total = 0
    #for num in numbers
    for num in numbers:
        #add num to total
        total += num
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
#definition product(*numbers)
def product(*numbers):
    #prod = 1
    pro = 1
    #for each number in numbers:
    for num in numbers:
        #produ = prod * number
        pro = pro * num
    #return produ
    return pro

#definition get_numbers()
def get_numbers():
    #numbers is empty list
    numbers = []
    #while true
    while True:
        number = input("Number: ")
        # Stop condition
        if number == "done":
            break
        # Check for negative integers
        if number.startswith("-") and number[1:].isdigit():
            numbers.append(int(number))
            continue
        # Check for positive integers
        if number.isdigit():
            numbers.append(int(number))
            continue
        # Check for floats (negative or positive)
        if number.count(".") == 1:
            left, right = number.split(".")
            # left side may be '-' or digits, right side must be digits
            if ((left.isdigit() or (left.startswith("-") and left[1:].isdigit()))
                and right.isdigit()):
                numbers.append(float(number))
                continue
    #return numbers
    return numbers

#definition main(operation,*numbers)
def main(operation, *numbers):
    if operation == "sum":
        return f"Result: {addition(*numbers)}"
    elif operation == "average":
        return f"Result: {average(*numbers)}"
    elif operation == "maximum":
        return f"Result: {maximum(*numbers)}"
    elif operation == "minimum":
        return f"Result: {minimum(*numbers)}"
    elif operation == "product":
        return f"Result: {product(*numbers)}"
    
        

#give instructions
print("This is a flexible calculator. You can preform 5 operations: sum, average, maximum, minimum, product.")
#while true
while True:
    #operation is ask what they would like to do
    operation = input("What would you like to do(put the name of the operation you would like to complete): ")
    #numbers is get_numbers()
    numbers = get_numbers()
    #print main(operation, numbers)
    print(main(operation,*numbers))
    #action = ask if would like to continue
    action = input("Would you like to complete another action: ")
    #if action is yes
    if action == "yes":
        #contiue
        continue
    #else
    else:
        #break
        break
#show thank you for using the flexible calculator
print("Thank you for using the flexible calculator.")


