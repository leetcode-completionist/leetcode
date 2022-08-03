class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
                [3,3,5,0,0,3,1,4]
            L:  [0,0,2,2,2,3,3,4], min: 0
                 -->
            R:  [4,4,4,4,4,4,3,0], max: 4
                             <--

        Intuition:
        - At every index, we can think of the above as two sub-arrays (i.e. left, right)
        - We want to find the max profit at left and max profit at right
        - The result will the be max possible sum of (left_profit, right_profit)

        Problem:
        - If we brute-force, at every index we will need to compute max profit
          (left + right) = N times

        Optimization:  
        - From left-to-right, we can keep track of max possible profit if we were to stop
          on any given day
        - From right-to-left, we can keep track of max possible profit if we were to start
          on any given day
        - For any given day, we calculate max possible profit to the left + max possible
          profit to the right
        
        Edge cases:
        - We can make UP TO 2 trades, so we have to account for a single trade to the left
          and a single trade to the right
        """
        n = len(prices)
        
        left_max_profit = [0] * n
        right_max_profit = [0] * n
        
        left_profit, right_profit = 0, 0
        min_price = prices[0]
        max_price = prices[-1]
        for i in range(1, n):
            # record max possible profit left-to-right
            min_price = min(prices[i], min_price)
            left_profit = max(left_profit, prices[i] - min_price)
            left_max_profit[i] = left_profit

            # record max possible profit right-to-left
            max_price = max(prices[n - i], max_price)
            right_profit = max(right_profit, max_price - prices[n - i])
            right_max_profit[n - i] = right_profit
            
        res = 0
        for i in range(-1, n):
            if i == -1:
                # we only make one trade from "right_max_profit"
                res = max(res, right_max_profit[i + 1])
            elif i == n - 1:
                # we only make one trade from "left_max_profit"
                res = max(res, left_max_profit[i])
            else:
                # we make two trades
                res = max(res,
                          left_max_profit[i] +
                          right_max_profit[i + 1])
        return res
