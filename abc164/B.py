import sys
from collections import deque
import copy
def main():
    A, B, C, D = map(int, input().split())
    while True:
        C -= B
        if C <= 0:
            print("Yes")
            sys.exit()
        A -= D
        if A <= 0:
            print("No")
            sys.exit()


if __name__ == '__main__':
    main()
