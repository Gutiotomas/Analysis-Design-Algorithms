from math import sqrt

numberCases = int(input())
for i in range(numberCases):
    numberHouses = int(input())
    j = sqrt((numberHouses**2 + numberHouses) / 2)
    if j == int(j):
        j = int(j)
        print(j)
    else:
        print("NO")
