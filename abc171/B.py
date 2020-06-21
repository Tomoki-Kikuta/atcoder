def main():
    N, K = map(int, input().split())
    p = [int(i) for i in input().split()]
    p.sort()
    ans = 0
    for i in range(K):
        ans += p[i]
    print(ans)


if __name__ == '__main__':
    main()
