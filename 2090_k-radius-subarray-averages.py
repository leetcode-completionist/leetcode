class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)
                
        res = [-1] * n
        
        window_size = 2 * k + 1
        
        if n < window_size:
            # impossible to get k-radius elements
            return res
        
        # Grab initial window
        window_sum = 0
        for i in range(window_size):
            window_sum += nums[i]
            
        # Middle of all possible k-radius subarrays
        min_i = k
        max_i = n - 1 - k
        
        for i in range(min_i, max_i + 1):
            # Record answer
            res[i] = window_sum // window_size
            
            # Subtract the last element
            # Add the latest element
            window_sum -= nums[i - k]
            next_i = i + k + 1
            if next_i < n:
                window_sum += nums[next_i]
                
        return res
