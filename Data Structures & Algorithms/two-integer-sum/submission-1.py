class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, num in enumerate(nums):
            
            complement=target-num
            if complement in seen:
                if i<seen[complement]:
                    return [i, seen[complement]]
                else:
                    return [seen[complement], i]
                    
            seen[num]=i
        