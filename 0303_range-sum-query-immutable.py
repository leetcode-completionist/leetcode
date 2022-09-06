# https://leetcode.com/problems/range-sum-query-immutable/
class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = []
        
        # create a prefix sum array
        for num in nums:
            if not self.sums:
                self.sums.append(num)
            else:
                self.sums.append(self.sums[-1] + num)


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            # left is 0, so we just need the sum up to right
            return self.sums[right]
        
        # otherwise, we subtract sums[left - 1] from sum
        # at right to extract the sum between [left, right]
        return self.sums[right] - self.sums[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
