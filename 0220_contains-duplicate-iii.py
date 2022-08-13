from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        sorted_list = SortedList()

        for i in range(len(nums)):
            if i > k:
                # we need to start evicting older entries from
                # our window
                sorted_list.remove(nums[i - k - 1])
            
            # if any element satisfies abs(nums[i] - element) <= t
            # then we will be on the left of it
            left = sorted_list.bisect_left(nums[i] - t)
            
            # if any element satisfies abs(element - nums[i]) <= t
            # then we will be on the right of it
            right = sorted_list.bisect_right(nums[i] + t)
            
            # if these pointers are ever different, then we have
            # at least one other element that satisfies the conditions
            if left != right:
                return True
            
            # add current number to the sorted list
            sorted_list.add(nums[i])

        return False
