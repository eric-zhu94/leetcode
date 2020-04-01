class Solution(object):
    def maxArea(self, height):
        s = 0
        e = len(height) - 1
        maxa = 0
        while s < e:
            maxa = max(maxa, min(height[s], height[e]) * (e-s))
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        return maxa
        
        """
        :type height: List[int]
        :rtype: int
        """
