def pair(N, k, sequence):
    sequence.sort()
    row = (k - 1) // N
    col = (k - 1) % N
    return sequence[row], sequence[col]

N, k = map(int, input().split())
sequence = [int(input()) for _ in range(N)]
result = pair(N, k, sequence)
print(result[0], result[1])