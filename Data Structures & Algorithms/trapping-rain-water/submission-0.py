class Solution:
    def trap(self, height: List[int]) -> int:
        l, r=0, len(height)-1
        left_max, right_max= 0, 0
        total=0

        while l<r:
            left_max=max(height[l], left_max)
            right_max=max(height[r], right_max)
            if left_max<right_max: 
                total+=left_max-height[l]
                l+=1
            else:
                total+=right_max-height[r]
                r-=1
        
        return total 
