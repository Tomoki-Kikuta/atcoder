def make_dp(W, K):
    dp = []
    for j in range(W + 1):
        dp.append([])
        for k in range(K + 1):
            dp[j].append(0)
    return dp


def cal_ans(N, W, K, dp, width, importance):
    for i in range(1, N + 1):
        # i - 1番目まで使った時
        for j in range(W, -1, -1):
            # 幅jを作る時
            for k in range(1, K + 1):
                # k枚使った時
                if width[i - 1] <= j:
                    dp[j][k] = max(dp[j][k],
                                   dp[j - width[i - 1]][k - 1]
                                   + importance[i - 1])
    return dp[W][K]


def main():
    W = int(input())
    N, K = map(int, input().split())
    width = []
    importance = []
    for i in range(N):
        a, b = map(int, input().split())
        width.append(a)
        importance.append(b)

    dp = make_dp(W, K)
    ans = cal_ans(N, W, K, dp, width, importance)
    print(ans)


if __name__ == "__main__":
    main()
