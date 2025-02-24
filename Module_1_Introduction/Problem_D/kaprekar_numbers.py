cases = int(input())
for _ in range(cases):
    num = int(input())
    square = num ** 2
    str_square = str(square)
    is_kaprekar = False
    len_square = len(str_square)    
    for i in range(1, len_square):
        parte_izq = int(str_square[:i]) if i > 0 else 0
        parte_der = int(str_square[i:]) if i < len_square else 0        
        if parte_izq + parte_der == num and parte_der != 0:
            is_kaprekar = True
            break    
    if is_kaprekar:
        print("KAP")
    else:
        print("NO")
