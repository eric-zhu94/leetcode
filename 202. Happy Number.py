class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        next_num = n
        while True:
            next_num = sum(map(lambda x:int(x) ** 2, str(next_num)))
            if next_num == 1:
                return True
            elif next_num in seen:
                return False
            else:
                seen.append(next_num)
        
        
        
        
        
