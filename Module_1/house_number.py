from math import sqrt

number_cases = int(input())
for case in range(number_cases):
    number_houses = int(input())
    house = sqrt((number_houses**2 + number_houses) / 2)
    if house == int(house):
        house = int(house)
        print(house)
    else:
        print("NO")
