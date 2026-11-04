class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxWater = 0
        while left<right:
            if heights[left]<=heights[right]:
                maxWater = max(maxWater, min(heights[left],heights[right])*(right-left))
                left+=1
            else:
                maxWater = max(maxWater, min(heights[left],heights[right])*(right-left))
                right-=1
        return maxWater

