from collections import Counter

def heir(num):
    num_str = str(num)
    n = len(num_str)
    
    if n % 2 != 0:
        return False
    
    half_len = n // 2
    num_digit_count = Counter(num_str)
    
    for i in range(10**(half_len-1), 10**half_len):
        if num % i == 0:
            j = num // i
            if len(str(i)) == half_len and len(str(j)) == half_len:
                combined_digit_count = Counter(str(i) + str(j))
                if combined_digit_count == num_digit_count:
                    return True
    return False

C = int(input())
for _ in range(C):
    num = int(input())
    if heir(num):
        print("Heredero")
    else:
        print("No")