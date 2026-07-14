class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count_s={}
        count_t={}
        for strs in s: 
            count_s[strs]=count_s.get(strs, 0)+1

        for q in t:
            count_t[q]=count_t.get(q, 0)+1
        return count_s==count_t
            
