class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*(len(temperatures))
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp,i))
                continue
            while stack and temp>stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i-stackI
            stack.append((temp,i))
        return res