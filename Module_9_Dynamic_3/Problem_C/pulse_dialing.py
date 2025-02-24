MOD = 1000000007

def pulse_dial(pulses):
    if pulses == 0:
        return 0
    
    dp = [0] * (pulses + 1)
    dp[0] = 1
    
    for i in range(1, pulses + 1):
        for digit in range(1, 10):
            if i == digit:
                dp[i] = (dp[i] + 1) % MOD
            if i > digit + 1:
                dp[i] = (dp[i] + dp[i - digit - 1]) % MOD
        
        if i >= 10:
            if i == 10:
                dp[i] = (dp[i] + 1) % MOD
            if i > 11:
                dp[i] = (dp[i] + dp[i - 11]) % MOD
    
    return dp[pulses]

test_cases = int(input())
for _ in range(test_cases):
    pulses = int(input())
    print(pulse_dial(pulses))