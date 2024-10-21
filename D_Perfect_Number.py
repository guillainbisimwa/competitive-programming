# Input the value of k
k = int(input())
count = 0
num = 19

while count < k:
    x = sum(map(int, str(num))) == 10
    if x:
        count += 1    
    if count == k:
        print(num)
        break
    
    num += 1
