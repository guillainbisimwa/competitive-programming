# Read input values
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def can_make_x_cookies(x):
    total_needed_powder = 0
    for i in range(n):
        required_amount = x * a[i]
        if required_amount > b[i]:
            total_needed_powder += required_amount - b[i]
        if total_needed_powder > k:  
            return False
    return total_needed_powder <= k

left, right = 0, 10**9 
max_cookies = 0

while left <= right:
    mid = (left + right) // 2
    if can_make_x_cookies(mid):
        max_cookies = mid  
        left = mid + 1
    else:
        right = mid - 1  
print(max_cookies)
