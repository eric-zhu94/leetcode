#https://leetcode.com/problems/check-if-n-and-its-double-exist/
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dbl = {}
        half = {}
        for num in arr:
            if num in dbl or num in half:
                return True
            dbl[num*2] = 0
            half[num/2] = 0
        return False


        
        
