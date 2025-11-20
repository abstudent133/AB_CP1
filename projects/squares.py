#AB 1st Squared Numbers
#list of numbers
numbers = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]
#new list is a list of map of list of numbers x itself
new_nums = list(map(lambda num: num**2, numbers))
#show the coordinating numbers
i = 0
for num in range(len(numbers)):
    print(f"Original: {numbers[i]} Squared: {new_nums[i]}")
    i += 1

