import math
def main():
    A, B, N = map(int, input().split())
    if B - 1 <= N:
        x = B - 1
    else:
        x = N
    ans = math.floor(A * x / B) - A * math.floor(x / B)
    print(ans)


if __name__ == '__main__':
    main()
