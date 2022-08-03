class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        # monotonically decreasing
        stack = []
        
        # start from the future and look back
        # like a true stock oracle ;)
        for i in range(len(prices) - 1, -1, -1):
            while stack and stack[-1] < prices[i]:
                # this means today's price is higher
                # than tomorrow's price
                #
                # to capture max profits in the future
                # we should sell today and buy tomorrow
                buy_price = stack.pop()
                
                if not stack:
                    # no more sell day
                    # no profit captured
                    break
                    
                # get the maximum sell price
                # since this is a monotonically decreasing stack
                # we pop the entire stack to capture
                # max profit
                sell_price = stack.pop()
                while stack:
                    sell_price = stack.pop()
                
                profit += sell_price - buy_price
            
            stack.append(prices[i])
        
        # process the rest of the stack with the same logic
        while stack:
            buy_price = stack.pop()
            if not stack:
                break
                
            sell_price = stack.pop()
            while stack:
                sell_price = stack.pop()

            profit += sell_price - buy_price
            
        return profit
