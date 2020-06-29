import sys
from collections import deque
import copy
import bisect
def main():
    N, M, K = map(int, input().split())
    MAX = 10 ** 9 + 7
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    A = []
    B = []
    A.append(0)
    B.append(0)
    for i in range(N):
        A.append(a[i] + A[i])
    for i in range(M):
        B.append(b[i] + B[i])
    B.append(B[M - 1] + MAX)
    ans = 0
    for i in range(N+1):
        if A[i] <= K:
            a = bisect.bisect_right(B, (K - A[i]))
            a -= 1
            ans = max(ans, (i + a))
    print(ans)

if __name__ == '__main__':
    main()
