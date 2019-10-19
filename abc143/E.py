INF = 10000000000
import math
def main():
    N, M, L = map(int, input().split())
    d = [[INF for i in range(N)] for j in range(N)]
    pre = [[i for i in range(N)] for j in range(N)]
    for i in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        if c > L:
            continue 
        d[a][b] = c
        d[b][a] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][j] > d[i][k] + d[k][j]:
                    pre[i][j] = k
                    d[i][j] = d[i][k] + d[k][j]
    #print(pre)
    Q = int(input())
    for i in range(Q):
        count = 0
        s, t = map(int, input().split())
        s -= 1
        t -= 1
        if d[s][t] == INF:
            print(-1)
        else:
            k = t
            distance = 0
            while pre[s][k] != s:
                k = pre[s][k]
                distance += d[t][k]
                if distance >= L:
                    distance -= L
                    count += 1
            print(count)



if __name__ == "__main__":
    main()