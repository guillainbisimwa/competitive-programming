# step1
t = int(input())
# array = [[1,8],[2,5],[1,2]]
# array = [[1,1],[2,5],[1,3],[2,6],[1,8],[1,4]]
array = []
for _ in range(t):
    x, y = list(map(int, input().split()))
    array.append([y, x])

array.sort()
#step2
min_amount = 0
left, right = 0, len(array)-1
# print(array)
while left <= right:
    min_amount = max(min_amount, array[left][0] + array[right][0])
    
    if array[left][1] < array[right][1]: amount = array[left][1]
    else: amount = array[right][1]
    
    array[left][1] -= amount
    array[right][1] -= amount
    
    if array[left][1] <= 0: left += 1
    if array[right][1] <= 0: right -= 1
    
print(min_amount)





# t = int(input())
# for _ in range()