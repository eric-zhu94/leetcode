#https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        #O(n) traversal solution
        cnt = {}
        for n in A:
            if n not in cnt:
                cnt[n] = 1
            elif cnt[n] >= 1:
                return n
            else:
                cnt[n] +=1
        
