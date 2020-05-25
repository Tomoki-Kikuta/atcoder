from itertools import combinations_with_replacement


def main():
    N, M, Q = map(int, input().split())
    combination = []
    for i in range(Q):
        a, b, c, d = map(int, input().split())
        a -= 1
        b -= 1
        combination.append((a, b, c, d))
    ans = []
    for p in combinations_with_replacement(list(range(1, M+1)), N):
        cnt = 0
        for a, b, c, d in combination:
            if p[b] - p[a] == c:
                cnt += d
        ans.append(cnt)

    print(max(ans))


if __name__ == '__main__':
    main()
