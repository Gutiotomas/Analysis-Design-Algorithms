def divide(arr):
    if len(arr) <= 1:
        if len(arr) == 1:
            print(arr[0])
        return arr
    mid = len(arr) // 2
    left = divide(arr[:mid])
    right = divide(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    print("".join(map(str, result)))
    return result

C = int(input())
cases = [input().strip() for _ in range(C)]

for idx, case in enumerate(cases, 1):
    print(f"caso {idx}:")
    arr = list(map(int, case.split()))
    divide(arr)
    if idx < C:
        print()