from collections import deque

def bfs(capacity, source, sink, parent):
    visited = [False] * len(capacity)
    queue = deque([source])
    visited[source] = True
    
    while queue:
        u = queue.popleft()
        
        for v in range(len(capacity)):
            if not visited[v] and capacity[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                
                if v == sink:
                    return True
    return False

def edmonds_karp(capacity, source, sink):
    parent = [-1] * len(capacity)
    max_flow = 0
    
    while bfs(capacity, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]
        
        max_flow += path_flow
    
    return max_flow

def solve():
    test_cases = int(input())
    
    for _ in range(test_cases):
        num_pipes, num_connections = map(int, input().split())
        capacity = [[0] * num_pipes for _ in range(num_pipes)]
        
        for _ in range(num_connections):
            u, v, c = map(int, input().split())
            capacity[u][v] += c
        
        max_flow = edmonds_karp(capacity, 0, num_pipes - 1)
        print(max_flow)

solve()