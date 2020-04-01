class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for c in nums:
            if len(str(c)) % 2 == 0:
                ans +=1
        return ans
        
