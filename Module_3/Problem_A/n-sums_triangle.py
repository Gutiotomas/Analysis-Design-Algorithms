from itertools import permutations

def count_valid_arrangements(nums, target):
    count = 0
    
    for perm in permutations(nums):
        side1 = perm[0] + perm[1] + perm[2] + perm[3]
        if side1 > target:
            continue
        
        side2 = perm[3] + perm[4] + perm[5] + perm[6]
        if side2 > target:
            continue
        
        side3 = perm[6] + perm[7] + perm[8] + perm[0]
        if side3 > target:
            continue
        
        if side1 == target and side2 == target and side3 == target:
            count += 1
    
    return count

cases = int(input())
for _ in range(cases):
    data = list(map(int, input().split()))
    target = data[0]
    nums = data[1:]
    
    result = count_valid_arrangements(nums, target)
    print(result)
