#https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordering = {}
        tmp = list(order)
        for i in range(len(tmp)):
            ordering[tmp[i]] = i
        for j in range(1, len(words)):
            first = words[j - 1]
            second = words[j]
            length = min(len(first), len(second))
            first_ptr = 0
            second_ptr = 0
            #Scenario 1: characters are same, increment and compare
            #Scenario 2: characters are different, w1 < w2, continue
            #Scenario 3: characters are different, w1 > w2, return false
            #Scenario 4: reached end of a word, compare length
            while first[first_ptr] == second[second_ptr]:
                #move to first different character
                first_ptr +=1
                second_ptr +=1
                if first_ptr >= length:
                    if len(first) > len(second):
                        return False
                    else:
                        break
            while first_ptr < length:
                if ordering[first[first_ptr]] > ordering[second[second_ptr]]:
                    return False
                else:
                    break
            if first_ptr >= length:
                if len(first) > len(second):
                    return False
                else:
                    break

        return True
            
            
        
