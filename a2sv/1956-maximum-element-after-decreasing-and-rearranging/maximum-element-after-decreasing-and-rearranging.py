class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        # 1st element == `1`
        arr[0] = 1

        #(abs(arr[i] - arr[i - 1]) <= 1) ???? nust
        result = 1
        for num in arr:
            result = min(result + 1, num)

        return result