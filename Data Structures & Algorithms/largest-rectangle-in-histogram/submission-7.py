class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i, height in enumerate(heights):
            #print("stack:", stack, res)
            #print("i:", i)
            start = i
            while stack and height<stack[-1][1]:
                stackInd, stackH = stack.pop()
                area = stackH * (i-stackInd)
                if area>res:
                    res = area
                start = stackInd
            stack.append((start,height))
        
        while stack:
            stackInd, stackH = stack.pop()
            area = stackH * (len(heights)-stackInd)
            if area>res:
                    res = area
        return res