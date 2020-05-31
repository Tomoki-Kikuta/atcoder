def dfs(v, time_, d, f, dp):
    if d[v] == 0:
        d[v] = time_
    for i in range(len(dp[v])):
        if d[dp[v][i]] == 0:
            time_ = dfs(dp[v][i], time_ + 1, d, f, dp)
    f[v] = time_ + 1
    return time_ +  1


def main():
    N = int(input())
    dp = [[] for i in range(N)]
    for i in range(N):
        line = [int(k) for k in input().split()]
        for j in range(len(line)):
            if j == 0 or j == 1:
                continue
            dp[line[0] - 1].append(line[j] - 1)

    d = [0] * N
    f = [0] * N
    time_ = 1
    for i in range(N):
        if d[i] == 0:
            time_ = dfs(i, time_, d, f, dp)
            time_ += 1
    for i in range(N):
        print(i + 1, d[i], f[i])

if __name__ == '__main__':
    main()
