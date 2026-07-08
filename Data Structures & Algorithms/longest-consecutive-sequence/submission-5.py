class Solution:
        def longestConsecutive(self, nums: List[int]) -> int:
            seen=set()
            longest=0
            for i in range(len(nums)):
                seen.add(nums[i])
            for num in seen:
                if num-1 not in seen:
                    length=1
                    current=num
                    c=current+1
                    
                    while c in seen:
                        length+=1
                        c+=1
                    longest=max(longest,length)

            return longest


        
            