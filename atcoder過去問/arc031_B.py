import numpy as np
import sys
import copy


def dfs(now_x, now_y, B):
    for x in range(-1, 2):
        for y in range(-1, 2):
            if (x + y) % 2 != 0:
                if B[now_x + x][now_y + y] == 1:
                    B[now_x + x][now_y + y] = -1
                    dfs(now_x + x, now_y + y, B)

def judge(now_x, now_y, A):
    B = copy.copy(A)
    dfs(now_x, now_y, B)
    for i in range(1, 11):
        for j in range(1, 11):
            if B[i][j] == 1:
                return False
    return True


def main():
    A = - np.ones((12, 12))
    for i in range(10):
        line = input()
        for j in range(len(line)):
            if line[j] == 'o':
                A[i + 1][j + 1] = 1
    
    for i in range(1, 11):
        for j in range(1, 11):
            if A[i][j] == -1:
                if judge(i, j, A):
                    print('YES')
                    sys.exit()
    print('NO')


if __name__ == "__main__":
    main()
