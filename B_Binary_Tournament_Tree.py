# def solve(l,r,d):
#     if l > r:
#         return
    
#     maxVal = max(a[l:r + 1])
#     maxIdx = a.index(maxVal)
#     depth[maxVal] = d
    
#     solve(l, maxIdx-1, d+1)
#     solve(maxIdx + 1, r, d+1)

# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     depth = []

#     solve(0, n-1, 0)
#     print(*[depth[val] for val in a])
# #
    
def solve(l, r, d):
    if l > r:
        return
    
    maxVal = max(a[l:r + 1])
    maxIdx = a.index(maxVal, l, r + 1) 
    depth[maxVal] = d
    solve(l, maxIdx-1, d+1)
    solve(maxIdx + 1, r, d+1)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    depth = [-1] * (max(a) + 1)  

    solve(0, n-1, 0)
    print(*[depth[val] for val in a])

