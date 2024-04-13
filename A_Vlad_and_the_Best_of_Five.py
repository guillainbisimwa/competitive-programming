t = int(input())

for i in range(t):
    s = input()
    
    count_A = s.count('A')
    count_B = s.count('B')
    
    if count_A > count_B:
        print('A')
    elif count_B > count_A:
        print('B')
    else:
        print('A')
