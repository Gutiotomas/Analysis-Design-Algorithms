from bisect import bisect_right

def towers(rad):
    stacks = []
    
    for radius in rad:
        pos = bisect_right(stacks, radius)
        
        if pos < len(stacks):
            stacks[pos] = radius
        else:
            stacks.append(radius)
    
    return len(stacks)

T = int(input())

for _ in range(T):
    rad = list(map(int, input().split()))
    print(towers(rad))