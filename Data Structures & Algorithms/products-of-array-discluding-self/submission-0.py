class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        suffix=1
        prefix=1
        i=0
        result=[1]*len(nums)
        for i in range(len(nums)):
            result[i]=prefix
            prefix *=nums[i]                
        
        j=i
        for j in range(len(nums)-1, -1, -1):
            result[j] = suffix * result[j]
            suffix *= nums[j]
           
        return result

            