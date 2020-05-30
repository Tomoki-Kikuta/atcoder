import copy


def main():
    N, K = map(int, input().split())
    a = [int(i) for i in input().split()]
    ans = 10 ** 11
    for i in range(1 << N):
        now = a[0]
        count = 0
        copy_a = copy.copy(a)
        for j in range(1, N):
            if i >> j & 1:
                count += max(now + 1 - a[j], 0)
                copy_a[j] = max(now + 1, a[j])
            now = max(now, copy_a[j])
        now = 0
        color = 0
        for j in range(N):
            if now < copy_a[j]:
                color += 1
                now = copy_a[j]
        if color >= K:
            ans = min(ans, count)
    print(ans)


if __name__ == '__main__':
    main()
