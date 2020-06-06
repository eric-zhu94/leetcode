#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        value = {'I': 1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
        subtract = {'I': 'VX', 'X':'LC', 'C':'DM'}
        chars = [c for c in s]
        if len(chars) == 1:
            return value[chars[0]]
        a_ptr = 0
        b_ptr = 1
        while a_ptr != len(chars):
            if a_ptr == len(chars) - 1:
                ans += value[chars[a_ptr]]
            elif chars[a_ptr] in 'IXC' and a_ptr < len(chars) - 1:
                if chars[b_ptr] in subtract[chars[a_ptr]]:
                    ans += value[chars[b_ptr]] - value[chars[a_ptr]]
                    a_ptr +=1
                    b_ptr +=1
                else:
                    ans += value[chars[a_ptr]]

            else:
                ans += value[chars[a_ptr]]
            a_ptr +=1
            b_ptr +=1
        return ans
