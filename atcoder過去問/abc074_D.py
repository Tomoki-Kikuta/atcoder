import sys


def main():
    N = int(input())
    A = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            dij = A[i][j]
            res = True
            for k in range(N):
                if k in [i, j]:
                    continue
                dikj = A[i][k] + A[k][j]
                if dij > dikj:
                    print(-1)
                    sys.exit()
                elif dij == dikj:
                    res = False
            if res:
                ans += dij
    print(ans)


if __name__ == '__main__':
    main()
