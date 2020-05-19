import sys
from collections import deque
import copy
def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    count = 0
    while K != N+2:
        if K == 1:
            min_ = 0
        if K >= 2:
            min_ = ((K * (K-1)) / 2) % MOD
        max_ = ((N + 1) * N - (N + 1 - K) * (N - K)) / 2 % MOD
        count += max_ - min_ + 1
        count %= MOD
        K +=1
    print(int(count))
    


if __name__ == '__main__':
    main()
