import sys
from collections import deque
import copy
def main():
    N, M = map(int, input().split())
    s = [[] for i in range(M)]
    for i in range(M):
        lines = [int(k) for k in input().split()]
        for j in range(len(lines)):
            if j == 0:
                continue
            s[i].append(lines[j] - 1)
    p = [int(i) for i in input().split()]
    ans = 0
    for i in range(1 << N):
        switchs = [0] * N
        flag = True
        for j in range(N):
            if (i >> j) & 1:
                switchs[j] = 1
        for k in range(M):
            count = 0
            for t in range(len(s[k])):
                if switchs[s[k][t]] == 1:
                    count += 1
            if count % 2 != p[k]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
