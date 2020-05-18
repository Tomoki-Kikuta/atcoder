import sys
from collections import deque
import copy
import heapq


def main():
    N = int(input())
    X = []
    Y = []
    color = [-1 for i in range(N)]
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    heap = []
    heapq.heappush(heap, (0, 0))
    count = 0
    while len(heap) != 0:
        d, now = heapq.heappop(heap)
        if color[now] == 1:
            continue
        color[now] = 1
        count += d
        for i in range(N):
            if color[i] == 1:
                continue
            a = min(abs(X[now] - X[i]), abs(Y[now] - Y[i]))
            heapq.heappush(heap, (a, i))
    print(count)


if __name__ == '__main__':
    main()
