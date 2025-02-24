import sys

num_test_cases = int(sys.stdin.readline())
for case_num in range(1, num_test_cases + 1):
    input_line = sys.stdin.readline().strip()
    if not input_line:
        continue

    bulbs = []
    for pair in input_line.split():
        serial, lumen = pair.split(':')
        bulbs.append((serial, int(lumen)))

    bulbs.sort(key=lambda x: x[0])

    serials = [bulb[0] for bulb in bulbs]
    lumens = [bulb[1] for bulb in bulbs]
    N = len(serials)

    INF = sys.maxsize
    dp = [[0 for _ in range(N)] for _ in range(N)]
    roots = [[0 for _ in range(N)] for _ in range(N)]

    for length in range(1, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1
            dp[i][j] = INF
            sum_lumens = sum(lumens[i:j+1])

            for r in range(i, j + 1):
                cost = 0
                if r > i:
                    cost += dp[i][r-1]
                if r < j:
                    cost += dp[r+1][j]
                cost += sum_lumens

                if cost < dp[i][j]:
                    dp[i][j] = cost
                    roots[i][j] = r

    def build_tree(i, j, depth):
        if i > j:
            return None
        r = roots[i][j]
        tree = {
            'serial': serials[r],
            'left': build_tree(i, r-1, depth + 1),
            'right': build_tree(r+1, j, depth + 1),
            'depth': depth
        }
        return tree

    tree = build_tree(0, N-1, 1)

    def print_tree(node, indent=""):
        if node is None:
            return
        print_tree(node['right'], indent + "\t")
        print(indent + node['serial'])
        print_tree(node['left'], indent + "\t")

    print(f"caso {case_num}:")
    print()
    print_tree(tree)
    if case_num < num_test_cases:
        print()