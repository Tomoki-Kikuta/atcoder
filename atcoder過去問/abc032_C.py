def main():
    N, K = map(int, input().split())
    list_ = []
    for i in range(N):
        a = int(input())
        list_.append(a)

    left = 0
    right = 0
    count = 0
    now = list_[left]
    max_count = 0
    while left >= 0 and right < N:
        if now <= K:
            count += 1
            max_count = max(max_count, count)
            right += 1
            if right == N:
                break
            now *= list_[right]
            if now == 0:
                max_count = N
                break
        else:
            count -= 1
            now /= list_[left]
            left += 1
            if left > right:
                right = left
                now = 1
    print(max_count)


if __name__ == "__main__":
    main()
