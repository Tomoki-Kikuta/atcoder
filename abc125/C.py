from fractions import gcd
import sys
sys.setrecursionlimit(4100000)

def main():
    N = int(input())
    A = [int(c) for c in input().split()]
    L = [0] * (N+1)
    R = [0] * (N+1)
    for i in range(N):
        L[i+1] = gcd(A[i],L[i])
    for i in range(N-1,-1,-1):
        R[i] = gcd(A[i],R[i+1])
    max_ = 0
    for i in range(0,N):
        max_ = max(gcd(L[i],R[i+1]), max_)
    print(max_)

if __name__ == "__main__":
    main()