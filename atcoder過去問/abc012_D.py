def warshall_floyd(dp, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


def cal_min_time(dp, N):
    max_time = max(dp[0])
    for i in range(1, N):
        max_time = min(max_time, max(dp[i]))
    return max_time

def main():
    N, M = map(int, input().split())
    dp = [[float("inf") * N for i in range(N)] for j in range(N)]
    for i in range(M):
        a, b, t = map(int, input().split())
        a -= 1
        b -= 1
        dp[a][b] = t
        dp[b][a] = t
    for i in range(N):
        dp[i][i] = 0
    warshall_floyd(dp, N)
    ans = cal_min_time(dp, N)
    print(ans)


if __name__ == '__main__':
    main()
