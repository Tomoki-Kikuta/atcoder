import sys
from collections import deque
import copy
def main():
    a, b, c, K = map(int, input().split())
    ans = 0
    ans += min(K, a)
    K -= a
    K -= b
    if K > 0:
        ans -= K
    print(ans)


if __name__ == '__main__':
    main()
