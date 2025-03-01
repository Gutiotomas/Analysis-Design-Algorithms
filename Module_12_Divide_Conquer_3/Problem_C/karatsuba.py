def four_subproducts(X, Y, N, level=1):
    if N == 1:
        return X * Y, [f"{X * Y}"]

    half_N = N // 2
    power_half_N = 10 ** half_N

    a = X // power_half_N
    b = X % power_half_N
    c = Y // power_half_N
    d = Y % power_half_N

    steps = []

    P1, steps_P1 = four_subproducts(a, c, half_N, level + 1)
    P2, steps_P2 = four_subproducts(a, d, half_N, level + 1)
    P3, steps_P3 = four_subproducts(b, c, half_N, level + 1)
    P4, steps_P4 = four_subproducts(b, d, half_N, level + 1)

    steps += steps_P1
    steps += steps_P2
    steps += steps_P3
    steps += steps_P4

    result = P1 * 10 ** N + (P2 + P3) * power_half_N + P4
    steps.append(f"{result}")

    return result, steps


def karatsuba(test_cases):
    results = []
    for i, (N, X, Y) in enumerate(test_cases):
        result = []
        result.append(f"caso {i + 1}:")

        final_result, intermediate_steps = four_subproducts(X, Y, N)

        result += intermediate_steps[:-1]

        result.append(f"{final_result}")

        results.append("\n".join(result))

    return "\n\n".join(results)

C = int(input())
test_cases = []
for _ in range(C):
    N, X, Y = map(int, input().split())
    test_cases.append((N, X, Y))

print(karatsuba(test_cases))