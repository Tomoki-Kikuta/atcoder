import sys
def main():
    N = int(input())
    S = input()
    now = 0
    count = 0
    while True:
        count += 1
        now_color = S[now]
        while now_color == S[now]:
            now += 1
            if now == N:
                print(count)
                exit()

if __name__ == "__main__":
    main()
