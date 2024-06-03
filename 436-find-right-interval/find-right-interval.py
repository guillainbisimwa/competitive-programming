class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = [[0, 0, 0] for _ in range(n)]

        for i in range(n):
            arr[i][0] = intervals[i][0]
            arr[i][1] = intervals[i][1]
            arr[i][2] = i

        arr.sort(key=lambda x: x[0])

        ans = [-1] * n
        for i in range(n):
            ans[arr[i][2]] = self.binary_search(arr, i, n - 1, arr[i][1])

        return ans

    def binary_search(self, arr, low, high, target):
        result = -1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid][0] >= target:
                result = arr[mid][2]
                high = mid - 1
            else:
                low = mid + 1

        return result