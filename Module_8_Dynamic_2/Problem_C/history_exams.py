def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

num_cases = int(input())
results = []

for case_num in range(1, num_cases + 1):
    num_exams = int(input())
    correct_order = list(map(int, input().split()))
    case_result = [f"caso {case_num}:"]
    for _ in range(num_exams):
        student_response = list(map(int, input().split()))
        lcs = lcs_length(correct_order, student_response)
        score = round((lcs / len(correct_order)) * 100)
        case_result.append(str(score))
    results.append("\n".join(case_result))

print("\n\n".join(results))
