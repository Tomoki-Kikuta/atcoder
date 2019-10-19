def main():
    A, B = map(int, input().split())
    B *= 2
    if A - B <= 0:
        print(0)
    else:
        print(A - B)
    

if __name__ == "__main__":
    main()
