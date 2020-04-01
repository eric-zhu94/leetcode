class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        le = len(nums)
        for i in range(le):
            if target - nums[i] in d.keys():
                return [d[target - nums[i]], i]
            d[nums[i]] = i
        return

        
