class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        answers = []

        for i in range(len(l)):
            subarray = nums[l[i]: r[i] + 1]
            subarray.sort()
            print(subarray)
            difference = subarray[1] - subarray[0]

            for j in range(2, len(subarray)):
                if subarray[j] - subarray[j - 1] != difference:
                    answers.append(False)
                    break
            else:
                answers.append(True)

        return answers

        