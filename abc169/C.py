import numpy as np
import sys
sys.setrecursionlimit(10 ** 9)
from decimal import Decimal
def main():
    a, b = map(Decimal, input().split())
    a = int(a)
    ans = a * b
    print(int(ans))


if __name__ == '__main__':
    main()
