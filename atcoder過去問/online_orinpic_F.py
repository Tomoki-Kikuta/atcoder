def warshall_floyd(dp, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


def main():
    n, k = map(int, input().split())
    dp = [[float("inf") for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for i in range(k):
        line_ = [int(i) for i in input().split()]
        if line_[0] == 0:
            a, b = line_[1] - 1, line_[2] - 1
            if dp[a][b] >= float("inf") * n:
                print(-1)
            else:
                print(dp[a][b])
        else:
            c, d, e = line_[1] - 1, line_[2] - 1, line_[3]
            if dp[c][d] > e:
                dp[c][d] = e
                dp[d][c] = e
                warshall_floyd(dp, n)


if __name__ == '__main__':
    main()
