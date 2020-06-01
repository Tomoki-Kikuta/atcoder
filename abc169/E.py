import sys
sys.setrecursionlimit(10000000)
import numpy as np


def main():
    N = int(input())
    Bs = []
    As = []
    for i in range(N):
        a, b = map(int, input().split())
        As.append(a)
        Bs.append(b)
    min_med = np.median(As)
    max_med = np.median(Bs)
    if N % 2 == 0:
        print(int(2 * (max_med - min_med) + 1))
    else:
        print(int((max_med - min_med) + 1))
    


if __name__ == '__main__':
    main()
