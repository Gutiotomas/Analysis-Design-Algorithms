import math
import heapq

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def min_spanning_tree(n, points):
    visited = [False] * n
    min_heap = []
    heapq.heapify(min_heap)
    total_length = 0.0
    heapq.heappush(min_heap, (0, 0))
    
    while min_heap:
        dist, u = heapq.heappop(min_heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        total_length += dist
        
        for v in range(n):
            if not visited[v]:
                d = distance(points[u], points[v])
                heapq.heappush(min_heap, (d, v))
    
    return total_length

t = int(input())

for _ in range(t):
    n = int(input())
    points = [tuple(map(float, input().split())) for _ in range(n)]
    
    result = min_spanning_tree(n, points)
    
    print(f"{result:.1f}")