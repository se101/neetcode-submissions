class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = []
        while left<=right:
            k = (left+right)//2
            hours = 0
            for p in piles:
                hours += math.ceil((p)/k)
                #print(hours,k)
            if hours>h:
                left=k+1
            elif hours<=h:
                res.append(k)
                right=k-1
        #print(res)
        return min(res)
                
