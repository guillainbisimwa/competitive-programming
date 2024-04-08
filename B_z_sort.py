
def zIndex(n, arr):

    arr.sort()
    ans = []
    i = 0 
    j = n - 1
    while i < j:
        ans.append(arr[i])
        ans.append(arr[j])
        i += 1
        j -= 1

    if i == j:
        ans.append(arr[j])

    print(*ans)

n = int(input())
arr = list(map(int,input().split()))

zIndex(n, arr)
