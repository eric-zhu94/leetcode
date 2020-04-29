https://leetcode.com/problems/robot-return-to-origin/
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ud = {'U': 1, 'D':-1}
        lr = {'L':-1, 'R': 1}
        x = 0
        y = 0
        for move in moves:
            if move in 'UD':
                y = y + ud[move]
            else:
                x = x + lr[move]
        if x == 0 and y == 0:
            return True
        else:
            return False
            
            
        
