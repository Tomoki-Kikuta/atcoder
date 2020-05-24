def main():
    N = int(input())
    S = input()
    a = [0, 0, 0]
    for i in range(N):
        if S[i] == 'R':
            a[0] += 1
        elif S[i] == 'G':
            a[1] += 1
        else:
            a[2] += 1
    count = a[0] * a[1] * a[2]
    for i in range(N - 1):
        for j in range(1, N):
            if i - j < 0 or N <= i + j:
                break
            if S[i - j] != S[i] and S[i] != S[i + j] and S[i - j] != S[i + j]:
                count -= 1
    print(count)


if __name__ == '__main__':
    main()
