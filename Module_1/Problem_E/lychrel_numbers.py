while True:
    number = int(input())    
    if number == 0:
        break    
    iteration = 0
    while iteration < 1000:
        if str(number) == str(number)[::-1]:
            print(iteration)
            break
        number = number + int(str(number)[::-1])
        iteration += 1
        if number >= 10**10:
            print("L")
            break