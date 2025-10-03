#AB 1st While Loops

for num in range(1,21):
    print(num)

num = 1
while num<= 20:
    print(num)
    num += 1

i = 0

while i < 20:
    i += 1
    if 1 == 10:
        print("i is 10")
        continue
    else:
        print(f"{i} iteration of the loop")
    # This is the incorrect spot i += 1
        