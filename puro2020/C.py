import sys
from collections import deque
import copy
import math
def main():
    N, K = map(int, input().split())
    a = [int(i) for i in input().split()]
    A = [0] * (N + 1)
    if K >= 41:
        for i in range(1, N+1):
            if i > 1:
                print(' ', end='')
            print(N, end='')
        print()
        sys.exit()
    for i in range(1, N+1):
        A[i] = a[i - 1]
    for _ in range(K):
        count = [0] * (N + 1)
        for i in range(1, N+1):
            left_d = max(math.ceil(i - A[i]), 1)
            right_d = min(math.floor(i + A[i]), N)
            count[left_d] += 1
            if right_d + 1 <= N:
                count[right_d + 1] -= 1
        for i in range(1, N+1):
            count[i] += count[i - 1]
        A = copy.copy(count)
    
    for i in range(1, N+1):
        if i > 1:
            print(' ', end='')
        print(A[i], end='')
    print()


if __name__ == '__main__':
    main()
