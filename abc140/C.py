def main():
    N = int(input())
    B = [int(i) for i in input().split()]
    A_sum = 0
    A = []
    A.append(B[0])
    for i in range(N-2):
        if B[i] < B[i+1]:
            A.append(B[i])
        else:
            A.append(B[i+1])
    A.append(B[N-2])
    
    for i in range(N):
        A_sum += A[i]
    print(A_sum)
        
if __name__ == "__main__":
    main()