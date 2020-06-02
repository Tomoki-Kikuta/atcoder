def fibonacci(N, dp):
    if dp[N] != 0:
        return dp[N]
    if N == 1 or N == 0:
        dp[N] = 1
    else:
        dp[N] = fibonacci(N - 1, dp) + fibonacci(N - 2, dp)
    return dp[N]


def main():
    N = int(input())
    dp = [0] * (N + 1)
    print(fibonacci(N, dp))


if __name__ == '__main__':
    main()
