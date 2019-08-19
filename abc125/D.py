def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    for i in range(N-1):
        if A[i] < 0:
            if A[i+1] <= 0:
                A[i] *= -1
                A[i+1] *= -1
            else:
                if abs(A[i]) > abs(A[i+1]):
                    A[i] *= -1
                    A[i+1] *= -1
        ##print(A[i])
    count = 0 
    for i in range(N):
        count += A[i]
    print(count)

if __name__ == "__main__":
    main()

