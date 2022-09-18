# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
class Solution:
    """
       Intuition:
       
           - You can only SELL if you were previously holding a stock

               max_profit if SOLD today is
               EQUAL TO the max_profit to HOLD a stock yesterday
               PLUS price today

               sell[i] = hold[i - 1] + price[i]

           - You can only COOLDOWN if you were previously cooling down already
             OR was selling a stock. (NOTE: we can cooldown indefinitely because
             we might want to wait for a cheaper price on a later day)

               max_profit if COOLDOWN today is
               EQUAL TO the MAX between:
                 - max_profit to COOLDOWN yesterday
                 - max_profit to SELL yesterday

               cooldown[i] = max(cooldown[i - 1], sell[i - 1])

           - You can only HOLD if you were previously holding already
             OR was in a cooldown. (NOTE: we can hold indefinitely because
             we might want to wait for a higher price on a later day)

               max_profit if HOLD today is
               EQUAL TO the MAX between:
                - max_profit to COOLDOWN yesterday MINUS the cost to buy today
                - max_profit to HOLD yesterday

               hold[i] = max(hold[i - 1], cooldown[i - 1] - price[i])
    
       DP Tabulation:

                           [   1,  2,  3,  0, 2]
               SELL  [-inf, -inf,  1,  2, -1, 3]  
               HOLD  [-inf,   -1, -1, -1,  1, 1]
           COOLDOWN  [   0,    0,  0,  1,  2, 2]
            
           NOTE: on day (-1), we initialize with base values. Since it is
                 impossible to SELL and HOLD on day (-1), we will use -inf.
            
       Results:
        
           On the last day, we will find the max(sell[i], hold[i], cooldown[i])
           for the max profit overall.
        
       Space Optimization:
        
           We will notice that we only need the max_profie from yesterday (i - 1) to 
           inform our decision today. So instead of a 2D table, we can simplify it to
           three temp variables.
    """
    def maxProfit(self, prices: List[int]) -> int:
        sell_max_profit = -math.inf
        hold_max_profit = -math.inf
        cooldown_max_profit = 0
        
        for price in prices:
            tmp = sell_max_profit
            
            sell_max_profit = hold_max_profit + price
            hold_max_profit = max(hold_max_profit, cooldown_max_profit - price)
            cooldown_max_profit = max(cooldown_max_profit, tmp)

        return max(sell_max_profit, hold_max_profit, cooldown_max_profit)
        
