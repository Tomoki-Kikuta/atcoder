import sys
from collections import deque
import copy
def main():
    A, V = map(int, input().split())
    B, W = map(int, input().split())
    T = int(input())
    can_A = V * T
    can_B = W * T
    if A < B:
        B += can_B
        A += can_A
        if A >= B:
            print('YES')
        else:
            print('NO')
    else:
        B -= can_B
        A -= can_A
        if A <= B:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
