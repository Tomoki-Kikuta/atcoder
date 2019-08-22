import heapq

def main():
    X,Y,Z,K = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    A.sort(reverse = True)
    B.sort(reverse = True)
    C.sort(reverse = True)
    heap = []
    heapq.heappush(heap,((A[0]+B[0]+C[0])*-1,0,0,0))
    for i in range(K):
        t = heapq.heappop(heap)
        print(t[0] * -1)
        if t[1] + 1 < len(A):
            if ((A[t[1]+1] + B[t[2]] + C[t[3]])*-1,t[1]+1,t[2],t[3]) not in heap:
                heapq.heappush(heap,((A[t[1]+1] + B[t[2]] + C[t[3]])*-1, t[1]+1,t[2],t[3]))
        if t[2] + 1 < len(B):
            if ((A[t[1]] + B[t[2]+1] + C[t[3]])*-1, t[1],t[2]+1,t[3]) not in heap:
                heapq.heappush(heap,((A[t[1]] + B[t[2]+1] + C[t[3]])*-1, t[1],t[2]+1,t[3]))
        if t[3] + 1 < len(C):
            if ((A[t[1]] + B[t[2]] + C[t[3]+1])*-1, t[1],t[2],t[3]+1) not in heap:
                heapq.heappush(heap,((A[t[1]] + B[t[2]] + C[t[3]+1])*-1, t[1],t[2],t[3]+1))

if __name__ == "__main__":
    main()