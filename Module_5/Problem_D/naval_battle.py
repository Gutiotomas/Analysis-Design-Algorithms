def min_torpedo_shots(test_cases):
    results = []
    
    for ships in test_cases:
        ships.sort(key=lambda x: x[1])
        
        shots = 0
        last_shot = -1
        
        for ship in ships:
            L, R = ship
            if L > last_shot:
                shots += 1
                last_shot = R
        
        results.append(shots)
    
    return results

test_cases = []
while True:
    N = int(input())
    if N == 0:
        break
    
    ships = []
    for _ in range(N):
        L, R = map(int, input().split())
        ships.append((L, R))
    
    test_cases.append(ships)

results = min_torpedo_shots(test_cases)

for result in results:
    print(result)