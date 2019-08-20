import sys

def main():
    N,K = [int(i) for i in input().split()]
    S = input()
    count = list()
    number = list()
    c = 0
    i = 0
    count.append(c)
    while i < N:
        now = S[i]
        if now == '1':
            number.append('1')
        else:
            number.append('0')
        while(S[i] == now):
            c += 1
            i += 1
            if i == N:
                break
        count.append(c)
    c = 0
    for i in range(len(number)):
        if number[i] == '0':
            c += 1
    if c <= K:
        print(len(S))
        sys.exit()
    else:
        max_c = 0
        i = 0
        while i < len(number):
            now = number[i]
            if now == '0' and i + 2 * K < len(count):
                max_c = max(max_c,count[i + 2 * K] - count[i])
            elif now == '1' and i + 2 * K + 1 < len(count):
                max_c = max(max_c,count[i + 2 * K + 1] - count[i])
            else:
                max_c = max(max_c,count[-1] - count[i])
            i += 1
        print(max_c)

if __name__ == "__main__":
    main()