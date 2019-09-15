def main():
    N,K,Q = [int(i) for i in input().split()]
    q_list = [0] * N
    for i in range(Q):
        a = int(input()) - 1
        q_list[a] += 1
    for i in range(N):
        if K - (Q - q_list[i]) > 0:
            print("Yes")
        else:
            print("No")
if __name__ == "__main__":
    main()