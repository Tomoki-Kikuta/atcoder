import sys
from collections import deque
import copy
INF = 10000000
def main():
    N, M, X = map(int, input().split())
    book = []
    ans = INF
    for i in range(N):
        info = [int(i) for i in input().split()]
        book.append(info)
    for i in range(1 << N):
        a = []
        for j in range(M + 1):
            a.append(0)    
        for j in range(N):
            if (i >> j) & 1:
                for t in range(M + 1):
                    a[t] += book[j][t]
        for j in range(1, M + 1):
            if a[j] < X:
                a[0] = INF
                break
        ans = min(ans, a[0])
    if ans >= INF:
        ans = -1
    print(ans)







if __name__ == '__main__':
    main()
