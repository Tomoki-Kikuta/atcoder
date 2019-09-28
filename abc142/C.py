def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [0 for i in range(N)]
    for i in range(N):
        B[A[i]-1] = i + 1
    for i in range(N):
        print(B[i],end = " ")
    print()

if __name__ == "__main__":
    main()