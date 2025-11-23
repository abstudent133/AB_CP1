#AB 1st Factoral Calculator

#print instructions
print("This is a factorial calculator. This means it will take any number you input and multiply each number after it. An example would be this: 5 is 5x4x3x2x1=120.")

#function for calculations(values)
def calc(*args):
    #num starts as 1
    num = 1
    #for each i in args
    for i in args:
        #multiply num by i
        num *= i
    #return num
    return num
    

#while true
while True:

    #while true:
    while True:

        #choice = input("factoral")
        choice = input("Number: ").strip()
       
        #if choice.isdigit
        if choice.isdigit():
            #turn input into a number
            choice = int(choice)
            #break
            break
        #else
        else:
            #if not a number
            print("That isn't a number...")
           
    #if choice == 0
    if choice == 0:
        #special case for 0 factorial
        print("0 = 1")
       
    else:
        #values is empty list
        values = []
        
        #n starts as choice
        n = choice

        #while n != 0
        while n != 0:
            #add n to values
            values.append(n)
            #n -= 1
            n -= 1

        #num = calc(*values)
        num = calc(*values)

        #print(num)
        print(num)
       

    #end = input("Would you like to quit")
    end = input("Would you like to quit(1 for yes, 2 for no): ").strip()
  
    #if end == "1"
    if end == "1":
        #if they want to quit
        break
    #else
    else:
        #otherwise pass
        pass

#print end message
print("Thank you for using the factorial calculator.")