n,k = map(int,input().split())
s = input()

h = 0
for i in range(n-1):
    if s[i] == s[i+1]:
        h+=1
print(min([n-1,h+2*k]))
