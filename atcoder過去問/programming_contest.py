def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                flag_i = False
                flag_j = False
                flag_k = False
                for t in range(N):
                    if not flag_i and S[t] == str(i):
                        flag_i = True
                    elif flag_i and not flag_j and S[t] == str(j):
                        flag_j = True                           
                    elif flag_i and flag_j and not flag_k and S[t] == str(k):
                        flag_k = True
                if flag_i and flag_j and flag_k:
                    ans += 1
    print(ans)


if __name__ == '__main__':
    main()
