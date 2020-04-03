class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        hi = float('-inf')
        ptr = 0
        local_max = 0
        for i in range(len(nums)):
            local_max = max(nums[i], nums[i] + local_max)
            if local_max > hi:
                hi = local_max
        return hi
                    
