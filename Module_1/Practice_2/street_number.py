while True:
    number_streets = int(input())
    if number_streets == 0:
        break
    total_sum = (number_streets * (number_streets + 1) * (2 * number_streets + 1)) // 6
    prefix_sum = [0] * (number_streets + 1)    
    for i in range(1, number_streets + 1):
        prefix_sum[i] = prefix_sum[i - 1] + i**2
    many_streets = 0
    for street in range(3, number_streets):
        left_sum = prefix_sum[street - 1]
        right_sum = total_sum - left_sum - street**2
        if left_sum != 0 and right_sum % left_sum == 0:
            many_streets += 1
    print(many_streets)
