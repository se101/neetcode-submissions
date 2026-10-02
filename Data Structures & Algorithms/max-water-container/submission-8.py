class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        left, right = 0, len(heights)-1
        while left<right:
            water = max(water, min(heights[left], heights[right])*(right-left))
            if heights[left]<=heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
            
        return water

