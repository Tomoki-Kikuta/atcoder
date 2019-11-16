def main():
    N = int(input())
    S = input()
    if N % 2 == 0:
        half = N // 2
        for i in range(half):
            A = S[i]
            B = S[i + half]
            if A != B:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
