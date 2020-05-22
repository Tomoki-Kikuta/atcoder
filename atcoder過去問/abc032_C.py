import sys


def main():
    N, K = map(int, input().split())
    list_ = []
    for i in range(N):
        a = int(input())
        if a == 0:
            print(N)
            sys.exit()
        list_.append(a)
    list_.append(10 ** 10)

    left = 0
    right = 0
    now = list_[left]
    max_count = 0
    while left < N:
        if now <= K:
            right += 1
            max_count = max(max_count, right - left)
            now *= list_[right]
        else:
            now //= list_[left]
            left += 1
            if left > right:
                right = left
                now = list_[left]
    print(max_count)


if __name__ == "__main__":
    main()
