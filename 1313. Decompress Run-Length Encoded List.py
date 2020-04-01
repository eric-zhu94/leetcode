class Solution(object):
    def decompressRLElist(self, nums):
        #iterative approach
        ans = []
        for i in range(1, len(nums),2):
            ans = ans + [nums[i]] * nums[i-1]
        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
