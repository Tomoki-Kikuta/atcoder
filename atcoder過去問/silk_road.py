import sys


def main():
    N, M = map(int, input().split())
    D = [0] * N
    C = [0] * M
    INF = 10 ** 10
    for i in range(N):
        d = int(input())
        D[i] = d
    for j in range(M):
        c = int(input())
        C[j] = c
    dp = [[INF for i in range(N + 1)] for j in range(M + 1)]
    for i in range(M+1):
        dp[i][0] = 0
    for i in range(1, M+1):
        for j in range(1, N+1):
            if i >= j:
                dp[i][j] = min(D[j - 1] * C[i - 1] + dp[i - 1][j - 1], dp[i - 1][j])
    print(int(dp[-1][-1]))


if __name__ == '__main__':
    main()
