class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        mapped = list(zip(position, speed))
        mapped.sort(reverse=True)
        for p, s in mapped:
            time = (target-p)/s
            if stack and time<=stack[-1]:
                continue
            else:
                stack.append(time)
            #print("stack:", stack)
        return len(stack)