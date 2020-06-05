def salesman(S, now_v, time_, N, dp, road):
    if dp[S][now_v] >= 0:
        return dp[S][now_v], 0
    if now_v == 0 and S == (1 << N) - 1:
        dp[S][now_v] = 0
        return dp[S][now_v], 0
    res = 10 ** 16
    count = 0
    for i in range(N):
        if not (S >> i & 1) and (time_ + road[now_v][i][0] <= road[now_v][i][1]):
            candidate, c = salesman(S | 1 << i, i, time_ + road[now_v][i][0], N, dp, road)
            candidate += road[now_v][i][0]
            if res > candidate:
                res = candidate
                count = 1
            elif res == candidate:
                count += 1
    dp[S][now_v] = res
    return dp[S][now_v], count


def main():
    N, M = map(int, input().split())
    if N == 1:
        print(0, 1)
        exit()
    INF = 10 ** 16
    road = [[[INF, 0] for i in range(N)] for j in range(N)]
    dp = [[-1 for i in range(N)] for j in range(1 << N)]
    for i in range(M):
        s, t, d, time_ = map(int, input().split())
        s -= 1
        t -= 1
        road[s][t] = [d, time_]
        road[t][s] = [d, time_]
    for i in range(N):
        for j in range(N):
            if i == j:
                road[i][j] = [0, INF]
    ans, count = salesman(0, 0, 0, N, dp, road)
    if ans >= INF:
        print("IMPOSSIBLE")
    else:
        print(ans, count)


if __name__ == '__main__':
    main()
