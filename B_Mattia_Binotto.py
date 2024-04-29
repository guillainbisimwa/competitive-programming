n = int(input())
arr = list(map(int, input().split()))

arr.sort()

wait = count = 0

for i in range(n):
    if wait < arr[i]:
        wait += arr[i]
        count +=1
print(count)