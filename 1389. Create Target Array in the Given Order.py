class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        l = 0
        for i in range(len(index)):
            if index[i] > l:
                ans.append(nums[i])
            else:
                ans.insert(index[i], nums[i])
            l += 1
        return ans
        
