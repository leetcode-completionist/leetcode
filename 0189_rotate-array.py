class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # reduces full loops
        k = k % n
        
        i = 0
        count = 0
        while count < n:
            # we expect to hit every element at least once
            current = i
            prev = nums[i]
            
            while True:
                # keep swapping elements until we reach back
                # our starting point "i"
                next_i = (current + k) % n
                nums[next_i], prev = prev, nums[next_i]
                current = next_i
                
                # increase the count every time we encounter a new
                # elemenbt
                count += 1
                
                if i == current:
                    # back to where we started, break out
                    break
            
            # increase our pointer to the next element
            i += 1
