def invert(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inv = invert(arr[:mid])
    right, right_inv = invert(arr[mid:])
    merged, split_inv = merge(left, right)
    return merged, left_inv + right_inv + split_inv

def merge(left, right):
    i, j = 0, 0
    merged = []
    split_inv = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            split_inv += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, split_inv

def win(cards):
    _, inversions = invert(cards)
    if inversions == 0:
        return "Empate"
    elif inversions % 2 == 1:
        return "Susana"
    else:
        return "Pedro"

while True:
    n = int(input().strip())
    if n == 0:
        break
    cards = [int(input().strip()) for _ in range(n)]
    print(win(cards))