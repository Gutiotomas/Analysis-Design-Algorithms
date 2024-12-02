def max_drinks(test_cases):
    for caps in test_cases:
        caps.sort(reverse=True)
        i, j = 0, len(caps) - 1
        drinks = 0
        
        while i < j:
            if caps[i] + caps[j] >= 1000:
                drinks += 1
                i += 1
                j -= 1
            else:
                j -= 1
            
        print(drinks)

cases = int(input())
test_cases = []

for _ in range(cases):
    caps_number = int(input())
    caps = []
    for _ in range(caps_number):
        cap = int(input())
        caps.append(cap)
    test_cases.append(caps)

max_drinks(test_cases)