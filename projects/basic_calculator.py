#AB 1st basic calculator

num1 = float(input("Give me one number:"))
num2 = float(input("Give me another number:"))

addition = (num1+num2)
subtraction = (num1-num2)
multiplication = (num1*num2)
division = (num1/num2)
floor_divison = (num1//num2)
modulo = (num1%num2)
exoponent = (num1**num2)



print(f"These are the answers to equations between the numbers {num1} and {num2}")
print(f"{num1} + {num2} = {addition:.2f}")
print(f"{num1} - {num2} = {subtraction:.2f}")
print(f"{num1} * {num2} = {multiplication:.2f}")
print(f"{num1} / {num2} = {division:.2f}")
print(f"{num1} // {num2} = {floor_divison}")
print(f"{num1} % {num2} = {modulo:.2f}")
print(f"{num1} ** {num2} = {exoponent:.2f}")
