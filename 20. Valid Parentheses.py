class Solution(object):
    def isValid(self, s):
        pairs = {'(':')', '{':'}', '[':']'}
        seen = []
        l = 0
        for c in s:
            if l == 0:
                seen.append(c)
                l += 1
            else:
                if c == pairs.get(seen[l - 1]):
                    seen.pop()
                    l -= 1
                else:
                    seen.append(c)
                    l += 1
        if l == 0:
            return True
        else:
            return False
            
        """
        :type s: str
        :rtype: bool
        """
        
