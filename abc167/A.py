import sys
from collections import deque
import copy
def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print('No')
            sys.exit()
    print('Yes')
 

if __name__ == '__main__':
    main()
