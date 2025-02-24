def findStatistic(arr, start, end, target, pivots):
    if start == end:
        return arr[start]
    else:
        pivot_index = choosePivot(start, end)
        partition_index = partition(arr, start, end, pivot_index)
        pivots.append(partition_index + 1)
        if target == partition_index:
            return arr[partition_index]
        elif target > partition_index:
            return findStatistic(arr, partition_index + 1, end, target, pivots)
        else:
            return findStatistic(arr, start, partition_index - 1, target, pivots)

def partition(arr, left, right, pivot_index):
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    i = left
    for j in range(left + 1, right + 1):
        if arr[j] < arr[left]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[left] = arr[left], arr[i]
    return i

def choosePivot(start, end):
    return start

def cases(target, sequence):
    length = len(sequence)
    target = target - 1
    pivots = []
    findStatistic(sequence, 0, length - 1, target, pivots)
    return pivots

while True:
    target = int(input().strip())
    if target == 0:
        break
    sequence = list(map(int, input().strip().split()))
    pivots = cases(target, sequence)
    print(" ".join(map(str, pivots)))