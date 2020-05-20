
def main():
    N, K = map(int, input().split())
    w = [0] * N
    p = [0] * N
    for i in range(N):
        w[i], p[i] = map(int, input().split())
    left = 0 # 可能
    right = 100 #不可能
    while left + 10 ** (-10) < right:
        mid = (left + right) / 2
        h = [0] * N
        for i in range(N):
            h[i] = (p[i] - mid) * w[i]
        h.sort(reverse=True)
        a = sum(h[0:K])
        if a >= 0:
            left = mid
        else:
            right = mid
    
    print(left)


if __name__ == '__main__':
    main()
