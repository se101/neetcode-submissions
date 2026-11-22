class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x//2
        if x==1:
            return 1
        res = 0
        while left<=right:
            middle = (left+right)//2
            if middle*middle<x:
                res = middle
                left = middle+1
            elif middle*middle>x:
                right = middle-1
            else:
                return middle
        return res