def main():
    N = int(input())
    d = [int(i) for i in input().split()]
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            count += d[i] * d[j]
    print(count)


if __name__ == "__main__":
    main()
