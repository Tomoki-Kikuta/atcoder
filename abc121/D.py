def main():
    A, B = map(int, input().split())
    continuous = 0
    a = 0
    b = 0
    c = 0
    if A % 2 == 0:
        continuous += int((B - A + 1) / 2)
    else:
        a = A
        continuous += int((B - (A + 1) + 1) / 2)
    if continuous % 2 != 0:
        c = 1
    if B % 2 != 1:
        b = B
    print(a ^ b ^ c)


if __name__ == "__main__":
    main()
