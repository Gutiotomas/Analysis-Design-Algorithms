DAY_TO_MINUTES = {
    "sabado": 0,
    "domingo": 1440,
    "lunes": 2880
}

def time_in_minutes(day, time_str):
    day_offset = DAY_TO_MINUTES[day]
    hours, minutes = map(int, time_str.split(':'))
    total_minutes = day_offset + hours * 60 + minutes
    return total_minutes

def solve_case(family_members):
    meetings = []
    for member in family_members:
        day, start_time, duration = member
        start_minutes = time_in_minutes(day, start_time)
        duration = int(duration)
        end_minutes = start_minutes + duration
        if start_minutes % 1440 >= 0 and start_minutes % 1440 < 360:
            continue
        if end_minutes % 1440 > 0 and end_minutes % 1440 < 360:
            continue
        meetings.append((start_minutes, end_minutes))
    
    meetings.sort(key=lambda x: x[1])
    
    count = 0
    last_end_time = -1
    for start, end in meetings:
        if start >= last_end_time:
            count += 1
            last_end_time = end
    
    return count

C = int(input())
results = []

for _ in range(C):
    F = int(input())
    family_members = []
    for _ in range(F):
        day, start_time, duration = input().split()
        family_members.append((day, start_time, duration))
    
    result = solve_case(family_members)
    results.append(result)

for res in results:
    print(res)
