from bisect import bisect_left


def main():
    n = int(input())
    a = [int(input()) for i in range(n)]

    INF = 10 ** 18
    dp=[INF for i in range(n)]
    for i in range(n):
        lower_index = bisect_left(dp, a[i])
        # print(lower_index)
        dp[lower_index] = a[i]
    print(n - bisect_left(dp, INF))
    #print(dp)


if __name__ == '__main__':
    main()

