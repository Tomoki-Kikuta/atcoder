import sys
import bisect
from collections import deque
import copy
def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    plus_list = []
    minus_list = []
    for i in range(N):
        plus_list.append((i+1) + A[i])
        minus_list.append((i+1) - A[i])
    plus_list.sort()
    minus_list.sort()
    count = 0
    for i in range(N):
        count += bisect.bisect_right(minus_list, plus_list[i]) - bisect.bisect_left(minus_list, plus_list[i])
    print(count)

if __name__ == '__main__':
    main()
