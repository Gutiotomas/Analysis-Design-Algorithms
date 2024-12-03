def min_soldiers_required(fortresses):
    fortresses.sort(key=lambda x: (-x[0], x[1] + x[2]))

    total_soldiers = 0
    current_soldiers = 0

    for S, K, B in fortresses:
        if current_soldiers < S:
            total_soldiers += (S - current_soldiers)
            current_soldiers = S

        current_soldiers -= K
        current_soldiers -= B

        if current_soldiers < 0:
            total_soldiers += abs(current_soldiers)
            current_soldiers = 0

    return total_soldiers

while True:
    N = int(input())
    if N == 0:
        break
    
    fortresses = []
    for _ in range(N):
        S, K, B = map(int, input().split())
        fortresses.append((S, K, B))
    
    print(min_soldiers_required(fortresses))
