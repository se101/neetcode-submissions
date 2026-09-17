class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        profit = 0
        while left<len(prices):
            while right<len(prices):
                print(left,right)
                if (prices[right]-prices[left])>profit:
                    profit=prices[right]-prices[left]
                right+=1
                print(profit)
            left+=1
            right=left+1
        return profit