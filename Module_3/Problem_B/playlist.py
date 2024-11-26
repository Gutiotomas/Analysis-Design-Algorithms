from itertools import combinations

def count_minutes(time, songs):
    minutes = len(songs)
    best_leftover = time
    
    for r in range(1, minutes + 1):
        for comb in combinations(songs, r):
            total_time = sum(comb)
            if total_time <= time:
                leftover_time = time - total_time
                best_leftover = min(best_leftover, leftover_time)
    
    return best_leftover

cases = int(input())
for _ in range(cases):
    data = list(map(int, input().split()))
    target = data[0]
    nums = data[1:]    
    result = count_minutes(target, nums)
    print(result)
