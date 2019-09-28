def main():
    N, K = [int(i) for i in input().split()]
    h = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1

    print(count)
if __name__ == "__main__":
    main()