class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False

def solve(test_cases):
    result = []
    
    for num_cities, num_roads, airport_cost, roads in test_cases:
        edges = []
        
        for city in range(num_cities):
            edges.append((airport_cost, city, num_cities))
        
        for city1, city2, road_cost in roads:
            edges.append((road_cost, city1 - 1, city2 - 1))
        
        edges.sort()

        uf = UnionFind(num_cities + 1)
        total_cost = 0
        airports_count = 0
        
        for cost, city1, city2 in edges:
            if uf.union(city1, city2):
                total_cost += cost
                if city2 == num_cities:
                    airports_count += 1
        
        result.append(f"{total_cost} {airports_count}")
    
    return result

num_test_cases = int(input())
test_cases = []
for _ in range(num_test_cases):
    num_cities, num_roads, airport_cost = map(int, input().split())
    roads = []
    for _ in range(num_roads):
        city1, city2, road_cost = map(int, input().split())
        roads.append((city1, city2, road_cost))
    test_cases.append((num_cities, num_roads, airport_cost, roads))

output = solve(test_cases)
for line in output:
    print(line)