def make_dp(N, W, K):
    dp = []
    for i in range(N + 1):
        dp.append([])
        for j in range(W + 1):
            dp[i].append([])
            for k in range(K + 1):
                dp[i][j].append(0)
    return dp


def cal_ans(N, W, K, dp, width, importance):
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            for k in range(1, K + 1):
                if width[i - 1] <= j:
                    dp[i][j][k] = max(dp[i - 1][j][k],
                                      dp[i - 1][j - width[i - 1]][k - 1]
                                      + importance[i - 1])
                else:
                    dp[i][j][k] = dp[i - 1][j][k]

    return dp[N][W][K]


def main():
    W = int(input())
    N, K = map(int, input().split())
    width = []
    importance = []
    for i in range(N):
        a, b = map(int, input().split())
        width.append(a)
        importance.append(b)

    dp = make_dp(N, W, K)
    ans = cal_ans(N, W, K, dp, width, importance)
    print(ans)


if __name__ == "__main__":
    main()
