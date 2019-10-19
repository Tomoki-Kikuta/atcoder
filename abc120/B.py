def main():
    A, B, K = map(int, input().split())
    count = 0
    number = min(A, B)
    while True:
        if A % number == 0 and B % number == 0:
            count += 1
            if count == K:
                break
        number -= 1
    print(number)


if __name__ == "__main__":
    main()
