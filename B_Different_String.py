# t = int(input())
 
 
# for _ in range(t):
#     a = input()
#     r = len(set(a))
#     if r == 1:
#         print("NO")
#     else:
#         print("YES")
#         x = a[-1] + a[:-1]
#         print(x)

# T = int(input())
 
# for _ in range(0, T):
# 	s = list(input())
 
# 	flag = []
# 	for i in range(len(s)):
# 		for j in range(i):
# 			t = list(s)
# 			t[i], t[j] = t[j], t[i]
# 			if (s != t):
# 				flag = T
# 				break
# 	if flag != []:
# 		print("YES")
# 		print("".join(t))
# 	else:
# 		print("NO")

# r = []
# for _ in range(int(input())):
#         s = input()
#         act = s[0]
#         dist = -1
#         l = [s[i] for i in range(len(s))]
#         for i in range(len(s)-1):
#                 if s[i+1] == act:
#                         act = s[i]
#                 else:
#                         dist = i
#                         l[i] = s[i+1]
#                         l[i+1] = s[i]
#                         break
#         if dist == -1:
#                 r.append('NO')
#         else:
#                 r.append('YES')
#                 a = ''
#                 for x in l:
#                         a += x
#                 r.append(a)
 
# print('\n'.join(r))


t=int(input())
 
def differ(s):
    n=len(s)
    ss=""
    flag=False
    for i in range(1,n):
        if s[0]!=s[i]:
            s=s[i]+s[1:i]+s[0]+s[i+1:]
            flag=True
            break           
    if flag:
        print("YES")
        print(s)
    else:
        print("NO")
    return 0
 
for i in range(t):
    s=input()
    differ(s)