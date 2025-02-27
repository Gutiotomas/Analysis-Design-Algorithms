MOD = 999999937

def fibMRP(a, b, c, d, N):
    if N == 1:
        return (1, 1, 1, 0)
    elif N % 2 == 0:
        a_prime, b_prime, c_prime, d_prime = fibMRP(a, b, c, d, N // 2)
        return (
            (a_prime * a_prime + b_prime * c_prime) % MOD,
            (b_prime * (a_prime + d_prime)) % MOD,
            (c_prime * (a_prime + d_prime)) % MOD,
            (d_prime * d_prime + b_prime * c_prime) % MOD
        )
    else:
        a_prime, b_prime, c_prime, d_prime = fibMRP(a, b, c, d, (N - 1) // 2)
        return (
            (a_prime * a_prime + b_prime * c_prime + b_prime * (a_prime + d_prime)) % MOD,
            (a_prime * a_prime + b_prime * c_prime) % MOD,
            (c_prime * (a_prime + d_prime) + d_prime * d_prime + b_prime * c_prime) % MOD,
            (c_prime * (a_prime + d_prime)) % MOD
        )

def fib(N):
    if N == 0:
        return 0
    elif N == 1:
        return 0
    _, b, _, _ = fibMRP(1, 1, 1, 0, N - 1)
    return b

def solve_fib(cases):
    results = []
    for N in cases:
        results.append(fib(N) % MOD)
    return results

C = int(input())
cases = [int(input()) for _ in range(C)]

results = solve_fib(cases)
for result in results:
    print(result)