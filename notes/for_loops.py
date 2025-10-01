#AB 1st For Loops

nums = [4,654,136,84,651,86,42,1,564,3,4894]

for num in nums:
    num /= 2
    if num > 100:
        print(f"{num} is only half {num*2}. It is a large number.")
    else:
        print(num)
print("Loop is over.")

for num in range(1,11):
    print(num)