n,t = list(map(int, input().split()))
l = list(map(int, input().split()))

s = 0
sumn = 0
m = 0
for e in range(n):
    sumn += l[e]
    while sumn > t and s <= 2:
        sumn -= l[s]
        s += 1
    m = max(m,e-s+1)
print(m)