def main():
    S = input()
    count = 0
    list_ = []
    for i in range(len(S)):
        if len(list_) == 0:
            list_.append(S[i])
        else:
            if S[i] != list_[-1]:
                count += 2
                list_.pop(-1)
            else:
                list_.append(S[i])
    print(count)


if __name__ == "__main__":
    main()
