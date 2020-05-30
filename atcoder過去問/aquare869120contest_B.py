def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    ans = 10 ** 12
    for i in range(N):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b
    for i in range(N):
        s = A[i]
        for j in range(N):
            f = B[j]
            if s > f:
                s, f = f, s
            count = 0
            for k in range(N):
                u, v = A[k], B[k]
                if u > v:
                    u, v = v, u
                count += f - s
                if u < s:
                    count += (s - u) * 2
                if f < v:
                    count += (v - f) * 2
            ans = min(ans, count)
    print(ans)


if __name__ == '__main__':
    main()
