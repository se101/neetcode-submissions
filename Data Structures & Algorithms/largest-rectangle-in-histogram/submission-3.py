class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i,height in enumerate(heights):
            stackind = i
            while stack and height<stack[-1][1]:
                stackind, stackheight = stack.pop()
                maxArea = max(maxArea, stackheight*(i-stackind))
            stack.append((stackind,height))
        while stack:
            maxArea = max(maxArea, stack[-1][1]*(len(heights)-stack[-1][0]))
            stack.pop()
        return maxArea