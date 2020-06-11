def cominit(MAX, MOD, fac, finv, inv):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i]= inv[MOD % i] * (MOD - MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD


def com(n, k, MOD, fac, finv):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    ans = fac[n] * (finv[k] * finv[n - k] % MOD) % MOD
    return int(ans)


def main():
    W, H = map(int, input().split())
    MOD = 10 ** 9 + 7
    height = H - 1
    width = W - 1
    MAX = height + width + 1
    fac = [0] * MAX
    finv = [0] * MAX
    inv = [0] * MAX
    cominit(MAX, MOD, fac, finv, inv)
    print(com(height + width, height, MOD, fac, finv))


if __name__ == '__main__':
    main()
