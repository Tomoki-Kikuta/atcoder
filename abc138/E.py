import sys
import bisect

def main():
    s = input()
    t = input()
    alphabets = dict.fromkeys(list("abcdefghijklmnopqrstuvwxyz"),None)
    for alphabet in alphabets:
        lists = []
        for j in range(len(s)):
            if alphabet == s[j]:
                lists.append(j)
        alphabets[alphabet] = lists
    now = -1
    count = 0
    for alphabet in t:
        if(len(alphabets[alphabet])==0):
            print(-1)
            sys.exit()
        else:
            lists = alphabets[alphabet]
            index = bisect.bisect_right(lists,now)
            if index >= len(lists):
                count += len(s)
                now = lists[0]
            else:
                now = lists[index]
    print(count + now + 1)

if __name__ == "__main__":
    main()