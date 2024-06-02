t = int(input())
while t:
    s = input()
    cuts = 0
    join = 0
    for i in range(len(s) - 1):
        cuts += s[i] != s[i + 1]
        if s[i] == "0" and s[i + 1] == "1":
            join = 1
    print(cuts + 1 - join)
    t -= 1