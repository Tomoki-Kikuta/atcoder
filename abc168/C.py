import sys
from collections import deque
import copy
import numpy as np
import math
def main():
    A, B, H, M = map(int, input().split())
    short = H * (360 / 12) + M * 1 / 2
    long_ = M * (360 / 60)
    ang = abs(long_ - short)
    ang = min(ang, 360 - ang)
    a = math.radians(ang)
    h = A * math.sin(a)
    w = B - A * math.cos(a)
    ans = math.sqrt(h ** 2 + w ** 2)
    print(ans)
    
    


if __name__ == '__main__':
    main()
