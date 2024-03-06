l1 = [6,7,8,9,10,11,12]
l2 = [6,20,8,30,10,11,13]

# LRU Cache method
# implement dictionnary

d = {}

for i in range(len(l1)):
    d[l1[i]] = 1

print(d)
count = 0

for i in l2:
    #if(d[i] == i):
    d[i] = d.get(i, 0)+1 # d[i]+1
    #count = count + 1

print(f"{count} times")

print(d)
