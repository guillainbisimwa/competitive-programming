testcase = int(input())
def validate(hit, arr, h):
    total = hit
    for idx in range(1, len(arr)):
            total += min(hit, arr[idx] - arr[idx - 1])
    return total >= h

for _ in range(testcase):
    n, h = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
        
    left = 0
    right = h + 1

    while  right > left + 1:
        mid = left + (right - left) // 2
        if validate(mid, arr, h):
            right = mid
        else:
            left = mid
    print(right)
# A2SV <> Remote G5F Camp I : Contest Analysis & Up-solving