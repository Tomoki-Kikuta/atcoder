import queue


def main():
    K = int(input())
    number_list = queue.Queue()
    for i in range(1, 10):
        number_list.put(i)
    count = 0
    number = 0
    while(count != K):
        number = number_list.get()
        if number % 10 != 0:
            number_list.put((10 * number) + (number % 10) - 1)
        number_list.put(10 * number + number % 10)
        if number % 10 != 9:
            number_list.put(10 * number + (number % 10) + 1)
        count += 1
    print(number)


if __name__ == "__main__":
    main()
