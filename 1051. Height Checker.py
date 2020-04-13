https://leetcode.com/problems/height-checker/
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #nlogn complexity due to sorting function
        #O(1) memory
        ans = 0
        s = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != s[i]:
                ans +=1
        return ans
        
