def quick_sort(array, start, end, counter):
    if start < end:
        pivot_index = divide(array, start, end)
        counter[0] += 1
        quick_sort(array, start, pivot_index - 1, counter)
        quick_sort(array, pivot_index + 1, end, counter)

def divide(array, start, end):
    pivot = array[start]
    i = start
    for j in range(start + 1, end + 1):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i], array[start] = array[start], array[i]
    return i

def recursion(array):
    counter = [0]
    quick_sort(array, 0, len(array) - 1, counter)
    return counter[0]

num_cases = int(input())
for _ in range(num_cases):
    array = list(map(int, input().split()))
    print(recursion(array))