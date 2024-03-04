def rearrange_array(n, arr):

    l = len(arr)/2 
    sum_first_half = sum(arr[:n])
    sum_second_half = sum(arr[n:])

    for i in range((n*2) - 1):
        # print(arr)
        # print()
        sum_first_half = sum(arr[:n])
        sum_second_half = sum(arr[n:])

        if sum_first_half != sum_second_half:
            return " ".join(map(str, arr))

        # swap
        for i in range((n*2) - 1):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    if sum_first_half == sum_second_half:
        return "-1" 


# Read input values
n = int(input())
arr = list(map(int, input().split()))

print(rearrange_array(n, arr))

# print(rearrange_array(3, [1,2,2,1,3,1]))
# TODO : FAILD ON TEST 6 
