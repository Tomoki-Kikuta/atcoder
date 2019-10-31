def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    left = 0
    right = 0
    now = -1
    count = 0
    while True:
        if now < A[right]:
            count += right - left + 1
        else:
            left = right
            count += 1
        right += 1
        now = A[right - 1]
        if right == N:
            break
    print(count)


if __name__ == "__main__":
    main()
