def main():
    N = int(input())
    MOD = 26
    ans = str()
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while N > 0:
        N -= 1
        ans = alpha[N % MOD] + ans
        N //= MOD
    print(ans)
        

if __name__ == '__main__':
    main()
