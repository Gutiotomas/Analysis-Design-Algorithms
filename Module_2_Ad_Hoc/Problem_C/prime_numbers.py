import math

MAX_LIMIT = 100000

def precompute_primes(limit):
    primes = []
    is_composite = [False] * limit
    prime_count_up_to = [0] * limit

    for i in range(2, limit):
        if not is_composite[i]:
            primes.append(i)
        prime_count_up_to[i] = len(primes)

        for j in range(len(primes)):
            if i * primes[j] >= limit:
                break
            is_composite[i * primes[j]] = True
            if i % primes[j] == 0:
                break

    return primes, prime_count_up_to

precomputed_primes, prime_count_up_to = precompute_primes(MAX_LIMIT)

def prime_error(numbers):
    count_of_primes = prime_count_up_to[numbers]
    expected_primes = round(numbers / math.log(numbers))
    error = count_of_primes - expected_primes
    return error

cases = int(input())
for _ in range(cases):
    numbers = int(input())
    print(prime_error(numbers))
