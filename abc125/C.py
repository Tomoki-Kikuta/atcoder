import math

def main():
    N = int(input())
    A = []
    for i in input().split():
        A.append(int(i))
    if N == 1:
        print(A[0])
    elif N == 2:
        print(max(A[0],A[1]))
    else:
        R = list()
        L = list()
        for i in range(N+1):
            R.append(0)
            L.append(0)
        for i in range(N):
            L[i+1] = math.gcd(A[i],L[i])
        for i in range(N-1,0,-1):
            R[i] = math.gcd(A[i],R[i+1])
        max_ = 0
        for i in range(N):
            max_ = max(math.gcd(L[i],R[i]), max_)
        print(max_)
        
if __name__ == "__main__":
    main()