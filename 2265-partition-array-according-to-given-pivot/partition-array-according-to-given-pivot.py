class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        leftArr = []
        rightArr = []

        pivotCnt = 0

        for num in nums:
            if num == pivot:
                pivotCnt += 1
            elif num < pivot:
                leftArr.append(num)
            else:
                rightArr.append(num)

        for i in range(pivotCnt):
            leftArr.append(pivot)

        leftArr.extend(rightArr)

        return leftArr
        