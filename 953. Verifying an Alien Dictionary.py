#https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {k:v for v,k in enumerate(order)}
        def compare(first, second, order):
            ptr = 0
            shorter = first if len(first) < len(second) else second
            while ptr < len(shorter):
                if order[second[ptr]] == order[first[ptr]]:
                    ptr += 1
                elif order[second[ptr]] < order[first[ptr]]:
                    return False
                else:
                    return True
            if shorter == first:
                return True
            return False
            
        start = 0
        end = 1
        while end < len(words):
            if not compare(words[start],words[end],hashmap):
                return False
            start +=1
            end +=1
        return True
            
            
        
