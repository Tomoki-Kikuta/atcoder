def main():
    N, M = map(int, input().split())
    pair = []
    for i in range(N):
        A, B = map(int, input().split())
        pair.append([A, B])
    pair.sort()
    count = 0
    money = 0
    now = 0
    while True:
        if pair[now][1] + count < M:
            money += pair[now][1] * pair[now][0]
            count += pair[now][1]
        else:
            money += (M - count) * pair[now][0]
            break
        now += 1
    print(money)


if __name__ == "__main__":
    main()
