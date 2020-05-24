import sys


def main():
    N = input()
    for i in N:
        if i == '7':
            print('Yes')
            sys.exit()
    print('No')



if __name__ == '__main__':
    main()
