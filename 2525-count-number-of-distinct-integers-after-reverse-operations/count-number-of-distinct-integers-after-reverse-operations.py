class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        set_integer = set()
        for num in nums:
            set_integer.add(num)
            val = 0
            bk = num
            while bk:
                val = val * 10 + (bk % 10)
                bk //= 10
            set_integer.add(val)
        return len(set_integer)