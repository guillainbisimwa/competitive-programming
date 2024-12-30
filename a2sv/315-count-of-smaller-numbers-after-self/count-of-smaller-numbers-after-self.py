class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = 20001
        freq = [0] * n

        for num in nums:
            adjusted_num = num + int(1e4)
            freq[adjusted_num] += 1

        sg = SegmentTree(n)
        sg.build(0, 0, n - 1, freq)

        ans = []
        for num in nums:
            adjusted_num = num + int(1e4)
            freq[adjusted_num] -= 1
            sg.update(0, adjusted_num, -1, 0, n - 1)
            count = sg.query(0, 0, n - 1, 0, adjusted_num - 1)
            ans.append(count)

        return ans
class SegmentTree:
    def __init__(self, n):
        self.seg = [0] * (4 * n)

    def build(self, index, low, high, arr):
        if low == high:
            self.seg[index] = arr[low]
            return
        mid = (low + high) // 2
        self.build(2 * index + 1, low, mid, arr)
        self.build(2 * index + 2, mid + 1, high, arr)
        self.seg[index] = self.seg[2 * index + 1] + self.seg[2 * index + 2]

    def query(self, index, low, high, l, r):
        # No overlap
        if r < low or high < l:
            return 0
        # Complete overlap
        if l <= low and high <= r:
            return self.seg[index]
        mid = (low + high) // 2
        left = self.query(2 * index + 1, low, mid, l, r)
        right = self.query(2 * index + 2, mid + 1, high, l, r)
        return left + right

    def update(self, index, i, val, low, high):
        if low == high:
            self.seg[index] += val
            return
        mid = (low + high) // 2
        if i <= mid:
            self.update(2 * index + 1, i, val, low, mid)
        else:
            self.update(2 * index + 2, i, val, mid + 1, high)
        self.seg[index] = self.seg[2 * index + 1] + self.seg[2 * index + 2]
