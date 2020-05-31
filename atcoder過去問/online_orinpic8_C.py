import sys
sys.setrecursionlimit(10 ** 7)
import numpy as np


def dfs(now_x, now_y, dp, count, ans):
    dp[now_x][now_y] = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if (x + y) % 2 == 0:
                continue
            next_x = now_x + x
            next_y = now_y + y
            if dp[next_x][next_y] == 1:
                ans = dfs(next_x, next_y, dp, count + 1, ans)
    ans = max(ans, count)
    dp[now_x][now_y] = 1
    return ans


def main():
    w = int(input())
    h = int(input())
    dp = np.zeros((h+2, w+2))
    for i in range(1, h+1):
        line = [int(k) for k in input().split()]
        for j in range(1, w+1):
            if line[j - 1] == 1:
                dp[i][j] = 1
    ans = 0
    for i in range(1, h+1):
        for j in range(1, w+1):
            if dp[i][j] == 1:
                ans = dfs(i, j, dp, 1, ans)
    print(ans)


if __name__ == '__main__':
    main()
