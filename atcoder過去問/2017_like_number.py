def sieve_of_eratosthenes(N):
    prime_list = [True] * (N + 1)
    prime_list[0] = prime_list[1] = False
    ans_list = [0] * (N + 1)
    for i in range(2, N+1):
        if prime_list[i]:
            for j in range(i*2, N+1, i):
                prime_list[j] = False
    for i in range(1, N+1):
        ans_list[i] = ans_list[i - 1]
        if i % 2 != 0:
            j = (i + 1) // 2
            if prime_list[i] and prime_list[j]:
                ans_list[i] += 1
    return ans_list

def main():
    ans_list = sieve_of_eratosthenes(10 ** 5)
    Q = int(input())
    for i in range(Q):
        l, r = map(int, input().split())
        print(ans_list[r] - ans_list[l - 1])

if __name__ == '__main__':
    main()
