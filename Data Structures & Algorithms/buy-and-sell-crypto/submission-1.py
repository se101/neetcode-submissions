class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left, right = 0, 1
        while left<len(prices)-1:
            while right<len(prices):
                profit = max(profit, prices[right]-prices[left])
                right+=1
            left+=1
            right = left+1
        return profit
