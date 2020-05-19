import sys
from collections import deque
import copy
def main():
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    count = sum(A)
    if N - count < 0:
        print(-1)
    else:
        print(N - count)


if __name__ == '__main__':
    main()
