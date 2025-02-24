import math

def precompute_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def generate_nunudon_sequence(limit):
    sequence = [1]
    while sequence[-1] <= limit:
        next_term = sequence[-1] + len(precompute_divisors(sequence[-1]))
        sequence.append(next_term)
    return sequence

def count_terms_in_range(sequence, a, b):
    count = 0
    for term in sequence:
        if a <= term <= b:
            count += 1
    return count

cases = int(input())
for _ in range(cases):
    a, b = map(int, input().split())
    sequence = generate_nunudon_sequence(b)
    result = count_terms_in_range(sequence, a, b)
    print(result)