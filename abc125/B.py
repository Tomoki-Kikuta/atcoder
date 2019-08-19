def main():
    N = int(input())
    V = list()
    C = list()
    for i in input().split():
        V.append(int(i))
    for i in input().split():
        C.append(int(i))
    answer = 0
    for i in range(N):
        if V[i] > C[i]:
            answer += V[i] - C[i]
    print(answer)

if __name__ == "__main__":
    main()