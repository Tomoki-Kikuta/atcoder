def cal_distance(m, n, MOD):
    if m == 1 or n == 0:
        return 1
    ans = 1
    while n != 1:
        if n % 2 == 1:
            ans = (ans * m) % MOD
        n //= 2
        m = (m ** 2) % MOD
    ans = (ans * m) % MOD
    return ans


def main():
    MOD = 10 ** 9 + 7
    N, Q = map(int, input().split())
    a = [int(i) for i in input().split()]
    c = [int(i) - 1 for i in input().split()]
    c.append(0)
    distance = [0] * N
    for i in range(1, N):
        distance[i] = distance[i - 1]
        distance[i] += cal_distance(a[i - 1], a[i], MOD)
    ans = 0
    now = 0
    for i in range(Q+1):
        next_ = c[i]
        ans += abs(distance[next_] - distance[now]) % MOD
        ans %= MOD
        now = next_
    print(ans % MOD)


if __name__ == '__main__':
    main()
