class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = collections.defaultdict(list)
        for w in strs:
            x = tuple(sorted(w))
            ana[x].append(w)
        ans = []
        for k in ana:
            ans.append(ana[k])
        return ans
