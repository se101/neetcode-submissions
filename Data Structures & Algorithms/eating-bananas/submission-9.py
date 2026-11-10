class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)
        while left<=right:
            middle = (left+right)//2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p/middle)
            if totalTime>h:
                left = middle+1
            else:
                res = middle
                right = middle-1
            print(middle, totalTime)
        return res 