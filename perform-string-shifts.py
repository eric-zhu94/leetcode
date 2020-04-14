https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        from collections import deque
        #naive solution, O(n), can optimise by taking mod of tot_shift to reduce number of shifts
        tot_shift = 0
        for sh in shift:
            if sh[0] == 0:
                tot_shift -= sh[1]
            else:
                tot_shift += sh[1]
        if tot_shift == 0:
            return s
        #use a deque for fast insertion at beginning / end 
        dq = deque(list(s))
        while tot_shift != 0:
            #left shifts
            if tot_shift < 0:
                dq.append(dq.popleft())
                tot_shift +=1
            else:
                dq.appendleft(dq.pop())
                tot_shift -=1
        return str(''.join(dq))
                
            
            
            
