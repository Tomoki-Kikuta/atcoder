import math

def cal(sum_, F, N, K, d):
    count = 0
    for i in range(N):
        if sum_[i] > d:
            count += math.ceil((sum_[i] - d) / F[i])
            if count > K:
                #作ることができない
                return False
    return True


def main():
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    F = [int(i) for i in input().split()]
    A.sort()
    F.sort(reverse=True)
    sum_ = []
    for i in range(N):
        sum_.append(A[i] * F[i])

    right = 10 ** 12
    left = 0
    count = 0
    pre_mid = 0
    while True:
        mid = (right + left) // 2
        if pre_mid == mid:
            break
        if cal(sum_, F, N, K, mid):
            # midを小さくすることができる
            right = mid
        else:
            # midを大きくしなければならない
            left = mid + 1
        pre_mid = mid
        count += 1
    print(mid)


if __name__ == "__main__":
    main()
