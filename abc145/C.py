import math


def main():
    N = int(input())
    x = []
    y = []
    total = 0
    
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    for i in range(N):
        now_x = x[i]
        now_y = y[i]
        for j in range(N):
            if i == j:
                continue
            total += math.sqrt(abs(now_x - x[j]) ** 2 + abs(now_y - y[j]) ** 2) * math.factorial(N - 1)
    print("{0:.7f}".format(total / math.factorial(N)))

if __name__ == "__main__":
    main()
