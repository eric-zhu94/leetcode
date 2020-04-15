 https://leetcode.com/problems/reverse-words-in-a-string-iii
 
 def reverseWords(self, s: str) -> str:
        #using inbuilt and reverse array functions
        #O(n)
        #s = s[::-1]
        #a = [word for word in s.split(' ')]
        #return ' '.join(a[::-1])
        
        #using own functions
        def strsplit(sentence):
            ar = []
            w = []
            for c in sentence:
                if c != ' ':
                    w.append(c)
                else:
                    ar.append(''.join(w))
                    w = []
            ar.append(''.join(w))
            return ar
        
        def reverse(word):
            x = list(word)
            start = 0
            end = len(word) - 1
            while start < end:
                x[start], x[end] = x[end], x[start]
                start +=1
                end -= 1
            return ''.join(x)
        
        z = strsplit(s)
        ans = []
        for word in z:
            ans.append(reverse(word))
        return ' '.join(ans)
