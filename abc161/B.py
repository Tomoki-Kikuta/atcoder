def main():
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    count = 0
    ok = 0
    for i in range(N):
        count += A[i]
    for i in range(N):
        if A[i] / count >= 1 / (4 * M):
            ok += 1
    if ok >= M:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
