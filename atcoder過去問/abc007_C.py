import sys
from collections import deque
import copy
import numpy as np


def main():
    h, w = map(int, input().split())
    s_y, s_x = map(int, input().split())
    g_y, g_x = map(int, input().split())
    dp = np.zeros((h, w))
    s_y -= 1
    s_x -= 1
    g_y -= 1
    g_x -= 1
    for i in range(h):
        line = input()
        for j in range(w):
            if line[j] == '#':
                dp[i][j] = -1
    queue = deque()
    queue.append((s_y, s_x))
    dp[s_y][s_x] = 1
    while len(queue) != 0:
        now_y, now_x = queue.popleft()
        for y in range(-1, 2):
            for x in range(-1, 2):
                if (x + y) % 2 == 0:
                    continue
                next_y = now_y + y
                next_x = now_x + x
                if dp[next_y][next_x] == 0:
                    dp[next_y][next_x] = dp[now_y][now_x] + 1
                    queue.append((next_y, next_x))
    print(int(dp[g_y][g_x] - 1))


if __name__ == '__main__':
    main()
