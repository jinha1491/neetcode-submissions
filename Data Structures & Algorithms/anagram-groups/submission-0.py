class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts={}
        for word in strs:
            count=[0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            key=tuple(count)
            
            if key not in dicts:
                dicts[key] = []

            dicts[key].append(word)
        return list(dicts.values())

