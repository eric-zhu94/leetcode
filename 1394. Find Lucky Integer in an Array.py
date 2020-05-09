#https://leetcode.com/problems/find-lucky-integer-in-an-array/
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        cnt = collections.Counter()
        for n in arr:
            cnt[n] +=1
        for k in cnt:
            if cnt[k] == k and k > ans:
                ans = k
        return ans
        
        
