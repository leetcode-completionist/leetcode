class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # memoize results base on target
        @cache
        def dfs(target: int) -> int:
            # base case of a target being reached
            # return a sum of 1
            if target == 0:
                return 1

            res = 0
            for num in nums:
                if target - num >= 0:
                    # for each possible target sum
                    # add up all possible ways
                    res += dfs(target - num)
            return res

        return dfs(target)
