class Solution(object):
    def strStr(self, haystack, needle):
        if needle == '':
            return 0
        else:
            l = len(needle)
            lh = len(haystack)
            if l > lh:
                return -1
            else:
                for i in range(lh - l + 1):
                    if haystack[i:i+l] == needle:
                        return i
                return -1

            
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
