def main():
    A, B, C = map(int, input().split())
    count = 0
    while B - A >= 0 and count < C:
        B -= A
        count += 1
    print(count)


if __name__ == "__main__":
    main()
