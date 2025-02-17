def divide_teams(tms):
    if len(tms) <= 1:
        return tms
    
    md = len(tms) // 2
    lft = divide_teams(tms[:md])
    rgt = divide_teams(tms[md:])
    
    return merge(lft, rgt)

def merge(lft, rgt):
    rslt = []
    i, j = 0, 0
    while i < len(lft) and j < len(rgt):
        if (lft[i][1] > rgt[j][1]) or (lft[i][1] == rgt[j][1] and lft[i][2] < rgt[j][2]) or (lft[i][1] == rgt[j][1] and lft[i][2] == rgt[j][2] and lft[i][0] < rgt[j][0]):
            rslt.append(lft[i])
            i += 1
        else:
            rslt.append(rgt[j])
            j += 1
    rslt.extend(lft[i:])
    rslt.extend(rgt[j:])
    return rslt

def marathon(lgs, R):
    tms = {}
    
    for entry in lgs:
        tm, prb, tm_time, rslt = entry
        if rslt == 'C':
            if tm not in tms:
                tms[tm] = {'solved': 0, 'penalty': 0, 'problems': {}}
            if prb not in tms[tm]['problems']:
                tms[tm]['problems'][prb] = {'solved': False, 'incorrect': 0, 'time': 0}
            if not tms[tm]['problems'][prb]['solved']:
                tms[tm]['problems'][prb]['solved'] = True
                penalty = tm_time + 20 * tms[tm]['problems'][prb]['incorrect']
                tms[tm]['solved'] += 1
                tms[tm]['penalty'] += penalty
                tms[tm]['problems'][prb]['time'] = tm_time
        elif rslt == 'I':
            if tm not in tms:
                tms[tm] = {'solved': 0, 'penalty': 0, 'problems': {}}
            if prb not in tms[tm]['problems']:
                tms[tm]['problems'][prb] = {'solved': False, 'incorrect': 0, 'time': 0}
            if not tms[tm]['problems'][prb]['solved']:
                tms[tm]['problems'][prb]['incorrect'] += 1
    
    tm_stats = []
    for tm, stats in tms.items():
        if stats['solved'] > 0:
            tm_stats.append((tm, stats['solved'], stats['penalty']))
    
    return divide_teams(tm_stats)

M = int(input())
for marathon_index in range(1, M + 1):
    R = int(input())
    lgs = []
    for _ in range(R):
        line = input().split()
        tm = int(line[0])
        prb = int(line[1])
        tm_time = int(line[2])
        rslt = line[3]
        lgs.append((tm, prb, tm_time, rslt))
    
    rnked_tms = marathon(lgs, R)
    
    print(f"maraton {marathon_index}:")
    for tm, solved, penalty in rnked_tms:
        print(f"{tm} {solved} {penalty}")
    if marathon_index < M:
        print()