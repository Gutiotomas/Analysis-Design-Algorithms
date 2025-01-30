def matrix_chain_order(dims):
    n = len(dims) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + dims[i] * dims[k+1] * dims[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    
    return s

def print_parentheses(s, i, j):
    if i == j:
        print(f'M{i+1}', end='')
    else:
        print('(', end='')
        print_parentheses(s, i, s[i][j])
        print(' x ', end='')
        print_parentheses(s, s[i][j] + 1, j)
        print(')', end='')

c = int(input())

for _ in range(c):
    dims = list(map(int, input().split()))
    s = matrix_chain_order(dims)
    print_parentheses(s, 0, len(dims) - 2)
    print()