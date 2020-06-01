import sys
from collections import deque
import copy
def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    for i in range(N):
        if A[i] == 0:
            print(0)
            sys.exit()
    count = 1
    for i in range(N):
        count *= A[i]
        if count > 10 ** 18:
            print(-1)
            sys.exit()
    print(count)

if __name__ == '__main__':
    main()
