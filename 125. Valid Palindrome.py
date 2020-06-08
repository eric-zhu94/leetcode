#https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #O(n) for passes through string
        s = s.lower()
        alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and s[start] not in alpha:
                start +=1
            while start < end and s[end] not in alpha:
                end -= 1
            if s[start] != s[end]:
                return False
            start +=1
            end -=1
        return True

        
