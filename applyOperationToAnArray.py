
def applyOperations(nums):
    
    i = 0
    arr = [0] * (len(nums))

    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0
            i += 1
        i += 1

    j = 0
    k = 0
    while j < len(nums):
        if nums[j] != 0:
            arr[k] = int(nums[j])
            k += 1
        j += 1
    return list(arr)

print(applyOperations([1,2,2,1,1,0]))


    

# Case 1
# Input
# nums =
# [1,2,2,1,1,0]
# Output
# [1,4,2]
# Expected
# [1,4,2,0,0,0]

# Input
# nums =
# [0,1]
# Output
# [1]
# Expected
# [1,0]