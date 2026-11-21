class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, height in enumerate(heights):
            stackI = i
            while stack and height<stack[-1][1]:
                stackI, stackH = stack.pop()
                area = stackH*(i-stackI)
                res = max(res, area)
            stack.append((stackI,height))
            #print("stack:", stack)
        while stack:
            stackI, stackH = stack.pop()
            area = stackH*(len(heights)-stackI)
            res = max(res, area)
        return res
