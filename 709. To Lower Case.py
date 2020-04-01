class Solution:
    def toLowerCase(self, str: str) -> str:
        up = ''
        ans = ''
        for c in str:
            x = ord(c)
            if x >= 65 and x <= 91:
                ans += chr(x + (32))
            else:
                ans += c
        return ans
