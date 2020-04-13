https://leetcode.com/problems/last-stone-weight/    
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) >1:
            y = stones.pop()
            x = stones.pop()
            if y != x:
                stones.append(y-x)
                #could do binary search for improvement rather than sorting each time
                stones.sort()
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
