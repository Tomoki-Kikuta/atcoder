import sys
import math


def is_prime(N):
    if N == 1:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True

def prime(N):
    prime = []
    is_prime = [True for i in range(N+1)]  # 全て素数であると初期化
    is_prime[0] = is_prime[1] = False # 0,1は素数ではない
    for i in range(2, N+1):
        if is_prime[i]:
            # iは素数である
            prime.append(i)
            for j in range(2 * i, N+1, i):
                # iの倍数は素数でない
                is_prime[j] = False
    # N以下の素数を表示
    return prime

def main():
    N = int(input())
    if N == 1:
        print(0)
        sys.exit()
    if is_prime(N):
        print(1)
        sys.exit()
    else:
        n = math.ceil(math.sqrt(N))
        prime_list = prime(n)
        ans = []
        for i in range(len(prime_list)):
            now = prime_list[i]
            j = 1
            while now ** j <= n:
                ans.append(now ** j)
                j += 1
        ans.sort()
        count = 0
        for i in range(len(ans)):
            now = ans[i]
            if N < now:
                break
            if N % now == 0:
                count += 1
                N //= now
        print(count)

if __name__ == '__main__':
    main()
