# https://leetcode.com/problems/count-number-of-bad-pairs/
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # j - i != nums[j] - nums[i]
        #
        # is equivalent to
        #
        # nums[i] - i != nums[j] - j
        #
        # If we want to find out how many bad pairs
        # has j as the first number: (j, ?)
        #
        # we will need to know how many
        # (nums[i] - i != nums[j] - j) exists.
        n = len(nums)
        
        # we first keep count of each (nums[i] - i)
        seen = defaultdict(int)
        for i in range(n):
            seen[nums[i] - i] += 1
            
        # then for each (nums[i] - i), n - value
        # will give us # of nums that would form
        # a bad pair
        bad = defaultdict(int)
        for k, v in seen.items():
            bad[k] = n - v
        
        # we sum up all bad pairs and divide in 2
        # to get the number of pairs
        res = 0
        for j in range(n):
            res += bad[nums[j] - j]
        return res // 2
