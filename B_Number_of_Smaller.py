def number_of_smaller(n, m, arr1, arr2):
    newArray = [0] * m
    i, j = 0, 0
    
    while j < m:
        if i < n:
            if arr1[i] < arr2[j]:
                i += 1
            else:
                newArray[j] = i
                j += 1
        else:
            newArray[j] = i
            j += 1
    
    return newArray

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = number_of_smaller(n, m, arr1, arr2)

print(*result)
