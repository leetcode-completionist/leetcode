# https://leetcode.com/problems/sliding-window-maximum/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        # monotonically decreasing queue
        # each value is a tuple (num, index)
        q = deque()
        
        for i in range(len(nums)):
            num = nums[i]
            
            # add to monotonic queue from the right
            while q and q[-1][0] < num:
                q.pop()
            q.append((num, i))
            
            while q and q[0][1] <= i - k:
                # evict older nums from list (from the left)
                q.popleft()
            
            if i >= k - 1:
                # first element is always largest in the window
                res.append(q[0][0])
        
        return res
