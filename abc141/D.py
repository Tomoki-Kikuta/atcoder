import heapq
import math

def main():
    N,M = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    count = 0
    heap = []
    for i in range(len(A)):
        heapq.heappush(heap,(A[i] * -1))
    for i in range(M):
        a = heapq.heappop(heap)
        a = int(a / 2)
        heapq.heappush(heap, a)
    for i in range(len(heap)):
        count += heapq.heappop(heap) * -1
    print(count)
    
if __name__ == "__main__":
    main()