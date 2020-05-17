import sys
from collections import deque
import copy
def main():
    X = int(input())
    now = 1
    for A in range(-118, 120):
        for B in range(-119, 118):
            if A ** 5 - B ** 5 == X:
                print(A, B)
                sys.exit()


if __name__ == '__main__':
    main()
