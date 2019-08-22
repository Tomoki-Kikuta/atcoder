def main():
    a = []
    for i in range(5):
        c = int(input())
        a.append(c)
    time = 0
    max_t = a[0]
    index = 0
    for i in range(5):
        if max_t % 10  > a[i] % 10 and a[i] % 10 != 0:
            max_t = a[i] 
            index = i
    for i in range(5):
        if i != index:
            while a[i] % 10 != 0:
                a[i] += 1
        time += a[i]
    print(time)


if __name__ == "__main__":
    main()