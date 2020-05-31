import sys
from collections import deque
import copy
def main():
    T = input()
    ans = str()
    for i in range(len(T)):
        if T[i] == '?':
            ans += 'D'
        else:
            ans += T[i]
    print(ans)


if __name__ == '__main__':
    main()
