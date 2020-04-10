def main():
    N, K = map(int, input().split())
    if N <= K:
        print(min(N, abs(N - K)))
    else:
        print(min(N % K, K - (N % K)))

if __name__ == "__main__":
    main()
