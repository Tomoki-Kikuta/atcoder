def main():
    A,B = [int(i) for i in input().split()]
    count = 0
    if A > B:
        count += A
        A -= 1
    else:
        count += B
        B -= 1
    count += max(A,B)
    print(count)


if __name__ == "__main__":
    main()