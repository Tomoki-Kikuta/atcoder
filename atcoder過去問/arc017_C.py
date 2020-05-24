from bisect import bisect_left, bisect_right


def main():
    N, X = map(int, input().split())
    W = [0] * N
    for i in range(N):
        w = int(input())
        W[i] = w
    half = N // 2
    w_conbination = []
    for i in range(1 << half):
        w = 0
        for j in range(half):
            if i >> j & 1:
                w += W[j]
        w_conbination.append(w)
    w_conbination.sort()

    ans = 0
    for i in range(1 << (N - half)):
        w = 0
        for j in range(N - half):
            if i >> j & 1:
                w += W[j + half]
        if X - w >= 0:
            ans += bisect_right(w_conbination, X - w) - bisect_left(w_conbination, X - w)
    print(ans)


if __name__ == '__main__':
    main()
