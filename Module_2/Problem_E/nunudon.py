import math

def precompute_divisors(limit):
    divisors = []
    for i in range(1, int(math.sqrt(limit)) + 1):
        if limit % i == 0:
            divisors.append(i)
            if i != limit // i:
                divisors.append(limit // i)
    return divisors

cases = int(input())
for _ in range(cases):
    limit = int(input())
    divisors = precompute_divisors(limit)
    print(len(divisors))