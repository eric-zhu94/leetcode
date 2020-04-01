class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
                continue
            seen[i] = 1
            
        for k, v in seen.items():
            if v == 1:
                return k
            
        return -1
