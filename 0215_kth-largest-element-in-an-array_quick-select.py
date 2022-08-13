class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Implement quick select
        #
        #     1. Pick a pivot (doesn't matter which, we will always use the middle)
        #
        #     2. Keep elements < pivot on the left, elements > pivot on the right.
        #        This is known as partitioning.
        #
        #     3. We will know by the end of the iteration which element we pick
        #
        #     4. If pivot == k, then we are done
        #
        #     5. If not, we go to either left or right depending on k value
        #
        # On average, the time complexity is O(n)
        # However, worst case, we would need O(n^2)
        n = len(nums)
        
        def partition(left, right, pivot) -> int:
            pivot_val = nums[pivot]
            
            # we move the pivot to the right of the partition first
            nums[right], nums[pivot] = nums[pivot], nums[right]
        
            # our element insertion starts at the left
            store_idx = left
        
            # then we iterate through every elements from left to
            # element right before the pivot
            for i in range(left, right):

                if nums[i] < pivot_val:
                    # element is less than pivot, we will store it to
                    # the left via store_idx
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    
                    # move our store_idx forward by one
                    store_idx += 1
            
            # whereever our store_idx is at the end of the iteration
            # is where our pivot value is supposed to be
            nums[store_idx], nums[right] = nums[right], nums[store_idx]
            
            # return the pivot's real position
            return store_idx
        
        
        def select(left, right) -> int:
            if left == right:
                # one element left, this is our target
                return nums[left]
            
            # pick the middle element as pivot (it can be random)
            pivot = (left + right) // 2
            
            # put the pivot in its rightful place
            pivot = partition(left, right, pivot)
            
            # pivot is in its rightful place
            # check if we found the kth largest
            # or need to perform another quick select
            if pivot == n - k:
                return nums[pivot]
            elif pivot < n - k:
                # pivot is less than kth largest
                # we look to the right
                return select(pivot + 1, right)
            else:
                # pivot is greater than kth largest
                # we look to the left
                return select(left, pivot - 1)
                
        # start quick select with the entire nums array
        return select(0, len(nums) - 1)
