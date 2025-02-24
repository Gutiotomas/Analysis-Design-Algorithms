import heapq

def min_friends_required(activities):
    if not activities:
        return 0
    
    activities.sort(key=lambda x: x[0])
    
    ongoing_activities = []
    
    for start, end in activities:
        if ongoing_activities and ongoing_activities[0] <= start:
            heapq.heappop(ongoing_activities)
        
        heapq.heappush(ongoing_activities, end)
    
    people_needed = len(ongoing_activities)
    
    return max(people_needed - 1, 0)

while True:
    N = int(input())
    if N == 0:
        break
    
    activities = []
    
    for _ in range(N):
        start, end = map(int, input().split())
        activities.append((start, end))
    
    print(min_friends_required(activities))