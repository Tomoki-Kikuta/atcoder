def main():
    N = int(input())
    i = 1
    count = 10000000000000
    while i * i <= N:
        if N % i == 0:
            A = N / i
            B = N / A
            count = min(count, (A - 1) + (B - 1))
        i += 1
    print(int(count))


if __name__ == "__main__":
    main()
