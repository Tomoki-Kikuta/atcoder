import sys
from collections import deque
import copy
def main():
    N = int(input())
    A = [(int(i) - 1) for i in input().split()]
    ans = [0 for i in range(N)]
    for i in range(len(A)):
        ans[A[i]] += 1
    for i in range(N):
        print(ans[i])


if __name__ == '__main__':
    main()
