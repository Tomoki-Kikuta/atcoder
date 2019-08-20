def main():
    N,K = [int(i) for i in input().split()]
    S = input()
    count = list()
    c = 0
    count.append(c)
    i = 0
    while i < N:
        now = S[i]
        while(S[i]==now):
            c += 1
            i += 1
            if i == N :
                break
        count.append(c)
    max_c = 0
    i = 0
    while i < N:
        now = S[i]
        if now == '0' and i + 2 * K < N:
            max_c = max(max_c,count[i + 2 * K] - count[i])
        elif now == '1' and i + 2 * K + 1 < N:
            max_c = max(max_c,count[i + (2 * K + 1)] - count[i])
        while(S[i]==now):
            i += 1
            if i == N:
                break
    print(max_c)
if __name__ == "__main__":
    main()