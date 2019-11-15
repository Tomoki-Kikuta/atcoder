def main():
    N = int(input())
    A = [int(c) for c in input().split()]

    max_A = sum(A)
    dp = [[False for i in range(max_A + 1)] for j in range(N + 1)]
    dp[0][0] = True

    for i in range(1, N + 1):
        for j in range(max_A + 1):
            if j < A[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] | dp[i - 1][j - A[i - 1]]
    
    print(sum(dp[N]))


if __name__ == '__main__':
    main()
