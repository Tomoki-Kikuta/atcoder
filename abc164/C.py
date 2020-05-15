import sys
from collections import deque
import copy
def main():
    N = int(input())
    S = []
    for i in range(N):
        s = input()
        S.append(s)
    S.sort()
    count = N
    for i in range(1, len(S)):
        if S[i - 1] == S[i]:
            count -= 1
    print(count)
    

if __name__ == '__main__':
    main()
