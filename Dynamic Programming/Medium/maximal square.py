def maximal_square(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_side = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '1':
                dp[r + 1][c + 1] = min(dp[r][c], dp[r + 1][c], dp[r][c + 1]) + 1
                max_side = max(max_side, dp[r + 1][c + 1])

    return max_side * max_side


m = [list(input().split()) for _ in range(int(input()))]
print(maximal_square(m))

