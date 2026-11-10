class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        mapped = list(zip(position, speed))
        mapped = sorted(mapped, reverse=True)
        for p,s in mapped:
            time = (target-p)/s
            if stack:
                if time>stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)
        return len(stack)