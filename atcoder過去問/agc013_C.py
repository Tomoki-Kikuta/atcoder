def main():
    N, L, T = map(int, input().split())
    collision = 0
    ants = []
    for i in range(N):
        x, w = map(int, input().split())
        if w == 1:
            collision += (x + T) // L
            a = (x + T) % L
        else:
            collision += (x - T) // L
            a = (x - T) % L
        ants.append(a)

    collision %= N
    ants.sort()
    ants = ants[collision:] + ants[:collision]
    for ant in ants:
        print(ant)


if __name__ == '__main__':
    main()
