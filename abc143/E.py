INF = 10000000000
import math
def main():
    N, M, L = map(int, input().split())

    d = [[INF for i in range(N)] for j in range(N)]
    ans_d = [[INF for i in range(N)] for j in range(N)]
    for i in range(N):
        d[i][i] = 0
        ans_d[i][i] = 0

    for i in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1 
        d[a][b] = c
        d[b][a] = c

    for k in range(N):
        for i in range(N):
            for j in range(N):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if d[i][j] <= L:
                ans_d[i][j] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                    ans_d[i][j] = min(ans_d[i][j], ans_d[i][k] + ans_d[k][j])

    Q = int(input())
    for i in range(Q):
        s, t = map(int, input().split())
        s -= 1
        t -= 1
        if d[s][t] == INF:
            print(-1)
        else:
            print(ans_d[s][t] - 1)



if __name__ == "__main__":
    main()