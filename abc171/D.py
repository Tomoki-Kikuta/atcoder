import sys
from collections import deque
import copy
def main():
    N = int(input())
    MAX = 10 ** 15
    A = [int(i) for i in input().split()]
    dict_num = {}
    num_sum = 0
    for i in range(N):
        if dict_num.get(A[i]) is None:
            dict_num[A[i]] = 1
        else:
            dict_num[A[i]] += 1
        num_sum += A[i]
    Q = int(input())
    for i in range(Q):
        b, c = map(int, input().split())
        if dict_num.get(b) is None:
            print(num_sum)
        elif dict_num[b] == 0:
            print(num_sum)
        else:
            num_sum += (c - b) * dict_num[b]
            print(num_sum)
            if dict_num.get(c) is None:
                dict_num[c] = dict_num[b]
            else:
                dict_num[c] += dict_num[b]
            dict_num[b] = 0



if __name__ == '__main__':
    main()
