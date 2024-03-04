def find_swaps(n, arr1, arr2):
    sorted_arr1 = sorted(arr1)
    sorted_arr2 = sorted(arr2)
    swaps = []
    for i in range(n):
        if arr1[i] != sorted_arr1[i] or arr2[i] != sorted_arr2[i]:
            for j in range(i + 1, n):
                if arr1[j] == sorted_arr1[i] and arr2[j] == sorted_arr2[i]:
                    swaps.append((j+1, i+1))
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                    arr2[i], arr2[j] = arr2[j], arr2[i]
                    break
            else:
                print(-1)
                return    

    print(len(swaps))
    for swap in swaps:
        print(" ".join(map(str, swap)))
    
    return


t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    find_swaps(n, arr1, arr2)
