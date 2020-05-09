#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        hi = max(candies)
        return [x + extraCandies >= hi for x in candies]
        
