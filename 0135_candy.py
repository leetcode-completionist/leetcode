class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Given an array: [2, 1, 4, 3,  2,  0,  0,  1]
        
        1. We traverse left to right to keep track of candies
           needed so that higher rated children will always have more
           candies than lower rated children on the left.
           
        2. Then we traverse righ to left to keep track of candies
           so that higher rated children will always have more
           candies than lower rated children on the right.
           
        3. The max(left[i], right[i]) will give us the minimum candies
           needed at "i" so that both lower rated children on left/right
           will have fewer candies.
        """
        n = len(ratings)
        
        # initialize arrays with 1 (i.e. every kid has at least 1 candy)
        left = [1] * n
        right = [1] * n
        
        for i in range(1, n):
            # from left
            if ratings[i] > ratings[i - 1]:
                # we need more candy than before
                left[i] = left[i - 1] + 1
            
            # from right
            if ratings[n - 1 - i] > ratings[n - i]:
                # we need more candy than before
                right[n - 1 - i] = right[n - i] + 1
        
        res = 0
        for i in range(n):
            res += max(left[i], right[i])
        return res
