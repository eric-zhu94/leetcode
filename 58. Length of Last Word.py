class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        le = 0
        for i in range(len(s) - 1, - 1, -1):
            if s[i] != ' ':
                le +=1
            elif le > 0:
                break
        return le


        
