#https://leetcode.com/problems/unique-morse-code-words/
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        uniq = []
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            s = ''
            for c in word:
                s = s + morse[ord(c) - ord('a')]
            uniq.append(s)
        return len(set(uniq))
            
        
