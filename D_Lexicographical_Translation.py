s = input()
sorted_s = sorted(s)
pointer = 0
u, t = [],[]

for i in s:
    while t and t[-1] == sorted_s[pointer]:
        u.append(t.pop())
        pointer +=1
    t.append(i)

u+= t[::-1]
print("".join(u))
