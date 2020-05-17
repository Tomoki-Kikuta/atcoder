import sys
from collections import deque
import copy
def main():
    N, M = map(int, input().split())
    dp = [[] for i in range(N)]
    color = [-1 for i in range(N)]
    distance = [10**5 for i in range(N)]
    color[0] = 0
    distance[0] = 0
    for i in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        dp[a].append(b)
        dp[b].append(a)
    queue = deque()
    queue.append((0, 0))
    while len(queue) != 0:
        now, d = queue.popleft()
        for i in range(len(dp[now])):
            if color[dp[now][i]] == -1 or distance[dp[now][i]] > d + 1:
                distance[dp[now][i]] = d + 1
                color[dp[now][i]] = now
                queue.append((dp[now][i], d + 1))
    for i in range(N):
        if color[i] == -1:
            print("No")
            sys.exit()
    print("Yes")
    for i in range(1, N):
        print(color[i] + 1)



if __name__ == '__main__':
    main()
