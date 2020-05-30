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
            count = 0
            for k in range(N):
                u, v = A[k], B[k]
                if u > v:
                    u, v = v, u
                if u <= s and v <= s:
                    count += abs(f - s) + abs(s - u) * 2
                elif u <= s and s <= v and v <= f:
                    count += abs(s - u) * 2 + abs(f - s)
                elif u <= s and f < v:
                    count += abs(s - u) * 2 + abs(f - s) + abs(v - f) * 2
                elif s <= u and u <= f and s <= v and v <= f:
                    count += abs(f - s)
                elif s <= u and u <= f and f <= v:
                    count += abs(f - s) + abs(v - f) * 2
                else:
                    count += abs(f - s) + abs(v - f) * 2
            ans = min(ans, count)
    print(ans)


if __name__ == '__main__':
    main()
