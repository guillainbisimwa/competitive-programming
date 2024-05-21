t = int(input())
 
for _ in range(t):
    p, m = list(map(int, input().split()))
    totalPeople = p + m
    possibleTeam = totalPeople // 4
    if min(p,m) < possibleTeam:
        print(min(p,m))
    else:
        print(possibleTeam)  