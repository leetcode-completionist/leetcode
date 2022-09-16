# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        
        # initialize dp of size m^2 (with extra row and col for base case)
        # the reason for this is at every mult, we always check 2 possibilities
        # so our DP table is m x m to capture our calculations
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        
		# start from the last multiplier and work backwards (bottom-up)
        for mult_idx in range(m - 1, -1, -1):
            for nums_l in range(mult_idx, -1, -1):
                # we can calculate nums_r on the fly using:
                # - mult_idx (how many numbers we've consumed)
                # - nums_l (how many numbers on the left we've consumed)
                # - n (how many nums are there in total)
                #
                # this is needed to not get memory-exceeded errors
                nums_r = n - 1 - (mult_idx - nums_l)

                dp[mult_idx][nums_l] = max(
                    # consume the num on the left
                    nums[nums_l] * multipliers[mult_idx] + dp[mult_idx + 1][nums_l + 1],
                    # consume the num on the right
                    nums[nums_r] * multipliers[mult_idx] + dp[mult_idx + 1][nums_l]
                )

        return dp[0][0]
