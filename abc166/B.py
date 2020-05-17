import sys
from collections import deque
import numpy as np
import copy
def main():
    N, K = map(int, input().split())
    dp = np.zeros(N)
    count = 0 
    for i in range(K):
        d = int(input())
        A = [int(t) - 1 for t in input().split()]
        for u in range(d):
            dp[A[u]] += 1
    for i in range(N):
        if dp[i] == 0:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
