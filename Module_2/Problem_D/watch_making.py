import math

def gcd_numbers(a, b, c):
    mcd_ab = math.gcd(a, b)
    mcd_total = math.gcd(mcd_ab, c)
    a = a // mcd_total
    b = b // mcd_total
    c = c // mcd_total
    sum = a + b + c
    return sum


cases = int(input())
for _ in range(cases):
    a, b, c = map(int, input().split())
    print(gcd_numbers(a, b, c))
