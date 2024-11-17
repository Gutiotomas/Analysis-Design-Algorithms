import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_numbers(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result

cases = int(input())

for _ in range(cases):
    numbers = list(map(int, input().split()))
    print(lcm_numbers(numbers))
