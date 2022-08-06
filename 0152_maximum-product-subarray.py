class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        low = [1]
        high = [1]

        for i, num in enumerate(nums):
            a = low[i] * num
            b = high[i] * num
            low.append(min(a, b, num))
            high.append(max(a, b, num))
        
        # ignore first value because
        # it was a placeholder
        return max(high[1:])
