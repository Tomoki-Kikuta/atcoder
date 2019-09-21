import heapq

def main():
    N = int(input())
    P = [int(i) for i in input().split()]
    count = 0
    for i in range(N-1):
        heap = []
        heapq.heappush(heap, P[i] * -1)
        for j in range(i+1,N):
            heapq.heappush(heap, P[j] * -1)
            A = heapq.heappop(heap)
            B = heapq.heappop(heap)
            count += B * -1
            heapq.heappush(heap,A)
            heapq.heappush(heap,B)
        
    print(count)


if __name__ == "__main__":
    main()