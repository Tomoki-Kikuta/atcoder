def main():
    S = input()
    count_0 = 0
    count_1 = 0
    for i in range(len(S)):
        ##0からスタート
        if i % 2 == 0 and S[i] != '0':
            count_0 += 1
        elif i % 2 == 1 and S[i] != '1':
            count_0 += 1
    for i in range(len(S)):
        ##1からスタート
        if i % 2 == 0 and S[i] != '1':
            count_1 += 1
        elif i % 2 == 1 and S[i] != '0':
            count_1 += 1
    print(min(count_0,count_1))

if __name__ == "__main__":
    main()