import numpy as np
def main():
    N, M = map(int, input().split())
    A = np.zeros((N, M))
    ans = 0
    for i in range(N):
        a = [int(k) for k in input().split()]
        for j in range(M):
            A[i][j] = a[j]
    for i in range(M-1):
        song_1 = i
        for j in range(i+1, M):
            count = 0
            song_2 = j
            for k in range(N):
                count += max(A[k][song_1], A[k][song_2])
            ans = max(ans, count)
    print(int(ans))


if __name__ == '__main__':
    main()
