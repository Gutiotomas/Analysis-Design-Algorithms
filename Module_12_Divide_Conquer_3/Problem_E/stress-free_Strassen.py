def matrix_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_mult(A, B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]

def matrix_sum(Z):
    return sum(sum(row) for row in Z)

def strassen(X, Y, N, depth=0):
    if N == 2:
        result = matrix_mult(X, Y)
        result_sum = matrix_sum(result)
        if depth > 0:
            print(result_sum)
        return result
    
    mid = N // 2
    A = [row[:mid] for row in X[:mid]]
    B = [row[mid:] for row in X[:mid]]
    C = [row[:mid] for row in X[mid:]]
    D = [row[mid:] for row in X[mid:]]
    
    E = [row[:mid] for row in Y[:mid]]
    F = [row[mid:] for row in Y[:mid]]
    G = [row[:mid] for row in Y[mid:]]
    H = [row[mid:] for row in Y[mid:]]
    
    P1 = strassen(A, E, mid, depth + 1)
    P2 = strassen(B, G, mid, depth + 1)
    P3 = strassen(A, F, mid, depth + 1)
    P4 = strassen(B, H, mid, depth + 1)
    P5 = strassen(C, E, mid, depth + 1)
    P6 = strassen(D, G, mid, depth + 1)
    P7 = strassen(C, F, mid, depth + 1)
    P8 = strassen(D, H, mid, depth + 1)
    
    Z11 = matrix_add(P1, P2)
    Z12 = matrix_add(P3, P4)
    Z21 = matrix_add(P5, P6)
    Z22 = matrix_add(P7, P8)
    
    Z = [[0] * N for _ in range(N)]
    for i in range(mid):
        for j in range(mid):
            Z[i][j] = Z11[i][j]
            Z[i][j + mid] = Z12[i][j]
            Z[i + mid][j] = Z21[i][j]
            Z[i + mid][j + mid] = Z22[i][j]

    if depth > 0:
        result_sum = matrix_sum(Z)
        print(result_sum)
    
    return Z

def process_case(case_num, X, Y, N):
    result = strassen(X, Y, N)
    print(matrix_sum(result))

C = int(input())
for case_num in range(1, C + 1):
    N = int(input())
    X = [list(map(int, input().split())) for _ in range(N)]
    Y = [list(map(int, input().split())) for _ in range(N)]
    
    print(f"caso {case_num}:")
    process_case(case_num, X, Y, N)
    if case_num < C:
        print()