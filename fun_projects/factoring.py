number = int(input("Give me a number you would like to factor:"))
factors = {
    1: ["1x1"],2: ["1x2"],3:["1x3"],4:["1x4,2x2"],5:['1x5'],6:['1x6,2x3'],7:['1x7']

}
print(factors[number])