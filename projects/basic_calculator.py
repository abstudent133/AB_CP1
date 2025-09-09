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
print(f"Addition: {addition:.2f}")
print(f"Subtraction: {subtraction:.2f}")
print(f"Multiplication: {multiplication:.2f}")
print(f"Division: {division:.2f}")
print(f"Floor Divison: {floor_divison}")
print(f"Modulo: {modulo:.2f}")
print(f"Exponent: {exoponent:.2f}")
