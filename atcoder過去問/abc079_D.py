def main():
    H, W = map(int, input().split())
    cost = 0
    digit = []
    for i in range(10):
        digit.append([])
        a = [int(i) for i in input().split()]
        digit[i] = a

    for k in range(10):
        for i in range(10):
            for j in range(10):
                digit[i][j] = min(digit[i][j], digit[i][k] + digit[k][j])

    for i in range(H):
        A = [int(i) for i in input().split()]
        for j in range(W):
            if A[j] >= 0:
                cost += digit[A[j]][1]
    print(cost)
    




if __name__ == "__main__":
    main()
