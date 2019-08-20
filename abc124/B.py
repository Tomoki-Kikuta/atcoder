def main():
    N = int(input())
    H = [int(i) for i in input().split()]
    count = 1
    max_H = H[0]
    for i  in range(1,N):
        if max_H <= H[i]:
            max_H = H[i]
            count += 1
    print(count)

if __name__ == "__main__":
    main()