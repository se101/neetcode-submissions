class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 1, max(candies)
        res = 0
        if k>sum(candies):
            return 0
        while left<=right:
            middle = (left+right)//2
            total = 0
            for candy in candies:
                total += candy//middle
            if total<k:
                right = middle-1
            else:
                res = max(res,middle)
                left = middle+1
        return res

