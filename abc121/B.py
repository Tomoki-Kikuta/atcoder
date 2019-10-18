def main():
    N, M, C = map(int, input().split())
    B = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        A = [int(i) for i in input().split()]
        total = 0
        for j in range(M):
            total += A[j] * B[j]
        total += C
        if total > 0:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
