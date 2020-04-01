class Solution(object):
    def numJewelsInStones(self, J, S):
        #n^2 solution - brute force nested for loops and counter
        #for i in J:
            #for j in S:
        cnt = 0
        for c in S:
            if c in J:
                cnt += 1
        return cnt
        
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
