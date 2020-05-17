import sys
from collections import deque
import copy
def main():
    N, M = map(int, input().split())
    H = [int(i) for i in input().split()]
    dp = [[] for i in range(N)]
    color = [0 for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        dp[a].append(b)
        dp[b].append(a)
    count = 0 
    for i in range(N):
        if color[i] == 1:
            continue
        flag = True
        for j in range(len(dp[i])):
            if H[i] <= H[dp[i][j]]:
                flag = False
                break
            else:
                color[dp[i][j]] = 1
        if flag:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
