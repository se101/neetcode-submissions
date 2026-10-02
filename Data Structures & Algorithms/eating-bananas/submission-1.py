class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)
        while left<=right:
            hours = 0
            middle = (left+right)//2
            for pile in piles:
                hours += math.ceil(pile/middle)
            if hours<=h:
                res = min(res, middle)
                right = middle-1
            elif hours>h:
                left = middle+1
        return res
