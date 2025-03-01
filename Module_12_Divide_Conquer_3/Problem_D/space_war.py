import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def split_pair(Px, Py, delta, best_pair):
    len_x = len(Px)
    mid_x = Px[len_x // 2][0]
    Sy = [p for p in Py if mid_x - delta <= p[0] <= mid_x + delta]
    best = delta
    len_y = len(Sy)
    
    for i in range(len_y - 1):
        for j in range(i+1, min(i + 8, len_y)):
            p, q = Sy[i], Sy[j]
            if p[2] != q[2]:
                dst = dist(p, q)
                if dst < best:
                    best = dst
                    best_pair = (p, q)
    
    return best, best_pair

def close_pair(Px, Py):
    if len(Px) <= 3:
        valid_pairs = [(dist(Px[i], Px[j]), (Px[i], Px[j])) 
                       for i in range(len(Px)) for j in range(i + 1, len(Px))
                       if Px[i][2] != Px[j][2]]
        if valid_pairs:
            return min(valid_pairs)
        else:
            return float('inf'), None

    mid = len(Px) // 2
    Qx = Px[:mid]
    Rx = Px[mid:]
    
    mid_x = Px[mid][0]
    Qy = list(filter(lambda x: x[0] <= mid_x, Py))
    Ry = list(filter(lambda x: x[0] > mid_x, Py))
    
    (dL, pairL) = close_pair(Qx, Qy)
    (dR, pairR) = close_pair(Rx, Ry)
    
    if dL < dR:
        delta = dL
        best_pair = pairL
    else:
        delta = dR
        best_pair = pairR
    
    (dS, pairS) = split_pair(Px, Py, delta, best_pair)
    
    if delta < dS:
        return delta, best_pair
    else:
        return dS, pairS

def rival_planets(planets):
    Px = sorted(planets, key=lambda x: x[0])
    Py = sorted(planets, key=lambda x: x[1])
    
    min_dist, _ = close_pair(Px, Py)
    
    if min_dist == float('inf'):
        return "INF"
    else:
        return f"{min_dist:.1f}"

while True:
    N = int(input())
    if N == 0:
        break
    
    planets = []
    for _ in range(N):
        x, y, faction = input().split()
        planets.append((int(x), int(y), faction))
    
    print(rival_planets(planets))