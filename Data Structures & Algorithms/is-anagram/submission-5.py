class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dicts={}
        dictss={}
        for strs in s: 
            dicts[strs]=dicts.get(strs, 0)+1

        for q in t:
            dictss[q]=dictss.get(q, 0)+1
        return dicts==dictss
            
