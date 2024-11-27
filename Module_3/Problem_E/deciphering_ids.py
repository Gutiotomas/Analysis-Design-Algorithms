from itertools import product

verification_letters = "TRWAGMYFPDXBNJZSQVHLCKE"

def dnis_count(dni):
    missing_positions = [i for i, c in enumerate(dni[:8]) if c == '?']    
    possible_digits = product('0123456789', repeat=len(missing_positions))
    
    count = 0
    for digits in possible_digits:
        possible_dni = list(dni[:8])
        for i, digit in zip(missing_positions, digits):
            possible_dni[i] = digit
        possible_dni_str = ''.join(possible_dni)
        
        number = int(possible_dni_str)
        remainder = number % 23
        if verification_letters[remainder] == dni[8]:
            count += 1
            
    return count

cases = int(input())

for _ in range(cases):
    dni = input().strip()
    print(dnis_count(dni))