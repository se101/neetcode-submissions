class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [[index, height],...]
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h<stack[-1][1]:
                stacki, stackh = stack.pop()
                maxArea = max(maxArea, stackh*(i-stacki))
                start=stacki
            stack.append([start,h])
        for i,h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea