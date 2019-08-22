import sys

def main():
    a = list()
    for i in range(5):
        t = int(input())
        a.append(t)
    k = int(input())
    for i in range(5):
        for j in range(i+1,5):
            if a[j] - a[i] > k:
                print(":(")
                sys.exit()
    print("Yay!")

if __name__ == "__main__":
    main()