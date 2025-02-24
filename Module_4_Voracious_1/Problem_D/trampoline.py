def trampoline_tantrums(children):
    children.sort(key=lambda x: (-x[1], x[0]))
    
    N = len(children)
    slots = [None] * N
    total_tantrums = 0
    
    for preferred_time, tantrum_time in children:
        p = preferred_time // 10
        
        while p >= 0 and slots[p] is not None:
            p -= 1
        
        if p >= 0:
            slots[p] = True
        else:
            for q in range(N-1, -1, -1):
                if slots[q] is None:
                    slots[q] = True
                    total_tantrums += tantrum_time
                    break
    
    return total_tantrums


t = int(input())
for _ in range(t):
    n = int(input())
    children = []
    
    for _ in range(n):
        t, p = map(int, input().split())
        children.append((t, p))
    
    result = trampoline_tantrums(children)
    print(result)