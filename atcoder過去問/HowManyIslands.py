import numpy as np
import sys
sys.setrecursionlimit(10 ** 6)


def dfs(now_x, now_y, dp):
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            next_x = now_x + x
            next_y = now_y + y
            if dp[next_x][next_y] == 1:
                dp[next_x][next_y] = 0
                dfs(next_x, next_y, dp)


def main():
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        dp = np.zeros((h+2, w+2))
        for i in range(1, h+1):
            line = [int(i) for i in input().split()]
            for j in range(1, w+1):
                if line[j - 1] == 1:
                    dp[i][j] = 1
        count = 0
        for i in range(1, h+1):
            for j in range(1, w+1):
                if dp[i][j] == 1:
                    count += 1
                    dp[i][j] = 0
                    dfs(i, j, dp)
        print(count)


if __name__ == '__main__':
    main()
