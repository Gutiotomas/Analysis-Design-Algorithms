def find_statistic(arr, left, right, k, indices):
    if left == right:
        indices.append(left + 1)
        return arr[left]
    else:
        pivot_index = left
        final_pivot_index = partition(arr, left, right, pivot_index)
        indices.append(final_pivot_index + 1)
        
        if k == final_pivot_index:
            return arr[final_pivot_index]
        elif k > final_pivot_index:
            return find_statistic(arr, final_pivot_index + 1, right, k, indices)
        else:
            return find_statistic(arr, left, final_pivot_index - 1, k, indices)

def partition(arr, start, end, pivot_index):
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    i = start
    for j in range(start + 1, end + 1):
        if arr[j] < arr[start]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[start] = arr[start], arr[i]
    return i

while True:
    k = int(input())
    if k == 0:
        break
    
    arr = list(map(int, input().split()))
    k -= 1
    
    indices = []
    find_statistic(arr, 0, len(arr) - 1, k, indices)
    
    print(" ".join(map(str, indices)))