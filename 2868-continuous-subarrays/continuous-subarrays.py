class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        num_subarrays = 1  
        left_boundary = nums[0] - 2  
        right_boundary = nums[0] + 2 
        start_index = 0 
        for end_index in range(1, len(nums)):
            if left_boundary <= nums[end_index] <= right_boundary:
                left_boundary = max(left_boundary, nums[end_index] - 2)
                right_boundary = min(right_boundary, nums[end_index] + 2)
            else:
                left_boundary = nums[end_index] - 2
                right_boundary = nums[end_index] + 2
                start_index = end_index
                while nums[end_index] - 2 <= nums[start_index] <= nums[end_index] + 2:
                    left_boundary = max(left_boundary, nums[start_index] - 2)
                    right_boundary = min(right_boundary, nums[start_index] + 2)
                    start_index -= 1
                start_index += 1
            num_subarrays += end_index - start_index + 1

        return num_subarrays