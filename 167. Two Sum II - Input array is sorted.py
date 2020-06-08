#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while True:
            x, y = numbers[start], numbers[end]
            if x + y == target:
                return [start + 1, end + 1]
            elif x + y > target:
                end -= 1
            else:
                start +=1
        return False
    
            
        
