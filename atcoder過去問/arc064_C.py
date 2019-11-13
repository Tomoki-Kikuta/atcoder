def main():
    N, x = map(int, input().split())
    A = [int(i) for i in input().split()]
    ans = 0
    for i in range(N - 1):
        if i == 0 and A[i] > x:
            ans += A[i] - x
            A[i] = x
        if A[i] + A[i + 1] > x:
            ans += A[i + 1] - (x - A[i])
            A[i + 1] = x - A[i]
    print(ans)


if __name__ == "__main__":
    main()
