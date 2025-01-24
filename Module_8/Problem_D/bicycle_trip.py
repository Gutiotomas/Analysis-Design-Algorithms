INF = float('inf')

def floyd_warshall(num_cities, matrix):
    dist = [[INF] * num_cities for _ in range(num_cities)]
    
    for i in range(num_cities):
        for j in range(num_cities):
            if matrix[i][j] != '-':
                dist[i][j] = int(matrix[i][j])
    
    for i in range(num_cities):
        dist[i][i] = 0
    
    for k in range(num_cities):
        for i in range(num_cities):
            for j in range(num_cities):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def find_longest_shortest_path(num_cities, matrix):
    dist = floyd_warshall(num_cities, matrix)
    
    max_dist = 0
    for i in range(num_cities):
        for j in range(i+1, num_cities):
            if dist[i][j] < INF:
                max_dist = max(max_dist, dist[i][j])
    
    return max_dist

while True:
    num_cities = int(input())
    if num_cities == 0:
        break
    
    matrix = []
    for _ in range(num_cities):
        matrix.append(input().split())
    
    print(find_longest_shortest_path(num_cities, matrix))
