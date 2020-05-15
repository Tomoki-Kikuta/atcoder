import sys
from collections import deque
import copy
def main():
    S, W = map(int, input().split())
    if S <= W:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
