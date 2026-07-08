class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts={}
        if len(s) != len(t):
            return False
        for c in s:
            dicts[c]=dicts.get(c, 0)+1
        for c2 in t:
            if c2 not in dicts:
                return False
            dicts[c2]-=1
            if dicts[c2] < 0:
                return False
        return True