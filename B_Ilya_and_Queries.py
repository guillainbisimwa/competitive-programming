s = input()
prefix = []
for i in range(len(s)-1):
    if s[i] == s[i+1]: 
        prefix.append(1)
    else:
        prefix.append(0)
prefix.append (1)

s = 0
for i in range(len(prefix)): 
    temp = prefix[i]
    prefix[i] = s 
    s += temp

for _ in range(int(input())):
    l, r= map(int, input().split())
    if l == 1:
        print(prefix[r-1])
    else:
        print(prefix[r-1] - prefix[l - 1])