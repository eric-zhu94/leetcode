class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        s = sum(nums)
        return int((l*(l+1) / 2) - s)

        
