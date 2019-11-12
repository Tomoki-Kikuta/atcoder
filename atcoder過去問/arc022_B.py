def main():
    N = int(input())
    A = [int(i) for i in input().split()]

    dict_number = {}
    for i in range(10 ** 5 + 1):
        dict_number[i] = 0

    max_count = 0
    right = 1
    dict_number[A[0]] += 1  
    for left in range(N):
        while right < N:
            if dict_number.get(A[right]) == 0:
                dict_number[A[right]] += 1
                right += 1
            else:
                break
        max_count = max(max_count, right - left)
        dict_number[A[left]] -= 1

    print(max_count)


if __name__ == "__main__":
    main()
