import sys
from collections import deque
import copy
def main():
    H, M, h, m, K = map(int, input().split())
    ans = 0
    while True:
        if H == h and M == m:
            break
        M += 1
        ans += 1
        if M == 60:
            M = 0
            H += 1
    print(ans - K)


if __name__ == '__main__':
    main()
