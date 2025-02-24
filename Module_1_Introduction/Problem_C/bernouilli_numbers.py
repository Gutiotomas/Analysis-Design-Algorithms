cases = int(input())
MOD = 49999
natural_numbers = 100
constant = 100

potencias_mod = [[0] * (constant + 1) for _ in range(natural_numbers + 1)]

for i in range(1, natural_numbers + 1):
    for p in range(1, constant + 1):
        potencias_mod[i][p] = pow(i, p, MOD)

for _ in range(cases):
    N, P = map(int, input().split())
    
    suma_mod = 0
    
    for i in range(1, N + 1):
        suma_mod = (suma_mod + potencias_mod[i][P]) % MOD
    
    print(suma_mod)
