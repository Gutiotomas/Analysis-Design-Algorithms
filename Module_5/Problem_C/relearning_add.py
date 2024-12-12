import heapq

def minimum_addition_cost(numbers):
    heapq.heapify(numbers)
    total_cost = 0
    while len(numbers) > 1:
        first = heapq.heappop(numbers)
        second = heapq.heappop(numbers)
        cost = first + second
        total_cost += cost
        heapq.heappush(numbers, cost)
    return total_cost

while True:
    N = int(input())
    if N == 0:
        break
    numbers = [int(input()) for _ in range(N)]
    print(minimum_addition_cost(numbers))