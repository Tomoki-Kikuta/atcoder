def salesman(T, now_v, dp, graph, v):
    if dp[T][now_v] >= 0:
        return dp[T][now_v]
    if T == (1 << v) - 1 and now_v == 0:
        dp[T][now_v] = 0
        return dp[T][now_v]
    res = 10 ** 7
    for i in range(v):
        if not ((T >> i) & 1):
            res = min(res, salesman(T | (1 << i), i, dp, graph, v) + graph[now_v][i])
    dp[T][now_v] = res
    return dp[T][now_v]


def main():
    v, e = map(int, input().split())
    INF = 10 ** 7
    graph = [[INF for i in range(v)] for j in range(v)]
    for i in range(e):
        s, t, d = map(int, input().split())
        graph[s][t] = d
    dp = []
    for i in range(1 << v):
        dp.append([])
        for j in range(v):
            dp[i].append(-1)
    salesman(0, 0, dp, graph, v)
    if dp[0][0] >= INF:
        print(-1)
    else:
        print(dp[0][0])


if __name__ == '__main__':
    main()
