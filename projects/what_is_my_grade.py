#AB 1st what is my grade

grade = round(float(input("Grade percentage: ")), 2)

if grade >= 93.00:
    print("You have an A.")
elif grade <= 92.9 and grade >= 90.0:
    print('You have an A-.')
elif grade <= 89.9 and grade >= 87.0:
    print("You have a B+.")
elif grade <= 86.9 and grade >= 83.0:
    print("You have a B.")
elif  grade <= 82.9 and grade >= 80.0:
    print("You have a B-.")
elif  grade <= 79.9 and grade >= 77.0:
    print("You have a C+.")
elif  grade <= 76.9 and grade >= 73.0:
    print("You have a C.")
elif  grade <= 72.9 and grade >= 70.0:
    print("You have a C-.")
elif  grade <= 69.9 and grade >= 67.0:
    print("You have a D+.")
elif  grade <= 66.9 and grade >= 63.0:
    print("You have a D.")
elif  grade <= 62.9 and grade >= 60.0:
    print("You have a D-.")
elif grade <= 59.9:
    print("You have an F.")
