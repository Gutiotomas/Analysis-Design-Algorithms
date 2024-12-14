import heapq

def dijkstra(maze, rows, cols):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cost = [[float('inf')] * cols for _ in range(rows)]
    cost[0][0] = 0  # Start with a cost of 0
    priority_queue = [(0, 0, 0)]  # Start with a cost of 0
    
    while priority_queue:
        current_cost, x, y = heapq.heappop(priority_queue)
        if x == rows - 1 and y == cols - 1:
            return current_cost
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < rows and 0 <= next_y < cols:
                new_cost = current_cost + maze[next_x][next_y]
                if new_cost < cost[next_x][next_y]:
                    cost[next_x][next_y] = new_cost
                    heapq.heappush(priority_queue, (new_cost, next_x, next_y))
    return cost[rows-1][cols-1]

test_cases = int(input())
for _ in range(test_cases):
    rows, cols = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(rows)]
    result = dijkstra(maze, rows, cols)
    print(result)