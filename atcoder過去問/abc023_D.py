def main():
    N = int(input())
    H = []
    S = []
    for i in range(N):
        h, s = map(int, input().split())
        H.append(h)
        S.append(s)
    left = 0
    right = 10 ** 15
    while left < right:
        mid = (left + right) // 2
        h = [0] * N
        for i in range(N):
            h[i] = ((mid - H[i]) / S[i])
        h.sort()
        flag = True
        for s in range(N):
            if s > h[s]:
                flag = False
                break
        if flag:
            right = mid
        else:
            left = mid + 1
    print(left)


if __name__ == '__main__':
    main()
