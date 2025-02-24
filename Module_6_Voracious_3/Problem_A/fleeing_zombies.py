import heapq

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if current_dist > dist[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return dist

N, M = map(int, input().split())
P = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))

distances = dijkstra(N, graph, 0)

for _ in range(P):
    destination = int(input())
    if distances[destination] == float('inf'):
        print("ZOMBI")
    else:
        print(distances[destination])
