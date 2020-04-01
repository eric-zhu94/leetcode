class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = {}
        t_seen = {}
        for i in range(len(s)):
            if s[i] not in s_seen:
                s_seen[s[i]] = 1
            else:
                s_seen[s[i]] +=1
        for j in range(len(t)):
            if t[j] not in t_seen:
                t_seen[t[j]] = 1
            else:
                t_seen[t[j]] +=1
        for k,v in s_seen.items():
            if len(s_seen) != len(t_seen):
                return False
            if k not in t_seen.keys():
                return False
            if v != t_seen[k]:
                return False
        return True 
            
