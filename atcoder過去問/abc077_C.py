import sys
from collections import deque
import copy
import bisect
def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    A.sort()
    B.sort()
    C.sort()
    count = 0
    for j in range(N):
        b = B[j]
        a = bisect.bisect_left(A, b)
        c = bisect.bisect_right(C, b)
        count += a * (N - c)
    print(count)


if __name__ == '__main__':
    main()
