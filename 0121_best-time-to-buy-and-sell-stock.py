class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        profit = 0
        for price in prices[1:]:
            if price < min_so_far:
                min_so_far = price
            profit = max(price - min_so_far, profit)
        
        return profit
