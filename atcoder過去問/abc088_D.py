import sys
from collections import deque
import numpy as np


def main():
    H, W = map(int, input().split())
    s_x = 1
    s_y = 1
    g_x = H
    g_y = W
    dp = - np.ones((H+2, W+2))
    black = 0
    for i in range(1, H+1):
        line = input()
        for j in range(1, W+1):
            if line[j - 1] == '.':
                dp[i][j] = 0
            else:
                black += 1
    queue = deque()
    queue.append((s_x, s_y))
    dp[s_x][s_y] = 1
    while len(queue) != 0:
        now_x, now_y = queue.popleft()
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x + y) % 2 == 0:
                    continue
                next_x = now_x + x
                next_y = now_y + y
                if dp[next_x][next_y] == 0:
                    dp[next_x][next_y] = dp[now_x][now_y] + 1
                    queue.append((next_x, next_y))
    if dp[g_x][g_y] == -1 or dp[g_x][g_y] == 0:
        print(-1)
    else:
        print(int(H * W - black - dp[g_x][g_y]))




if __name__ == '__main__':
    main()
