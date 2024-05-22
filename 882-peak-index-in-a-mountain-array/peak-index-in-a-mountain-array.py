class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            cur = left + (right - left) // 2
            if arr[cur] > arr[cur + 1] and arr[cur] > arr[cur - 1]:
                return cur
            if arr[cur] > arr[cur + 1]:
                right = cur - 1
            else:
                left = cur + 1
        return -1