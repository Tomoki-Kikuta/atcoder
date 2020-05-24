import sys
from collections import deque
import copy
from math import gcd
def main():
    K = int(input())
    a = []
    for i in range(1, K+1):
        for j in range(1, K+1):
            a.append(gcd(i, j))
    count = 0
    for i in range(1, K+1):
        for j in range(len(a)):
            count += gcd(i, a[j])
    print(count)


if __name__ == '__main__':
    main()
