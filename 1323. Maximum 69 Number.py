class Solution:
    def maximum69Number (self, num: int) -> int:
            v = list(str(num))
            for c in range(len(v)):
                if v[c] == '6':
                    v[c] = '9'
                    break
                else:
                    continue
            return ''.join(v)
        
