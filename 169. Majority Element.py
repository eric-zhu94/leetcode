class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import math
        seen = {}
        maj = math.floor(len(nums) / 2)
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 1
            else:
                seen[nums[i]] +=1
            if seen[nums[i]] > maj:
                return nums[i]
        
