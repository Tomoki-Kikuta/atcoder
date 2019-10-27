def main():
    A, B = map(int, input().split())
    if A >=10 or B >= 10:
        print(-1)
    elif A <= 0 or B <= 0:
        print(-1)
    else:
        print(A * B) 


if __name__ == "__main__":
    main()
