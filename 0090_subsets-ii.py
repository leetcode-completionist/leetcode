class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort the numbers so we can detect duplicates
        nums.sort()

        n = len(nums)
        dp = [[] * i for i in range(n)]

        # start from the back
        for i in range(n - 1, -1, -1):
            if i < n - 1 and nums[i] == nums[i + 1]:
                # Number is same as before, we only create
                # subsets from previous results.
                #
                # Input:       [2,2,3]
                # i:            0
                # DP:          [
                #               [],
                #               [[2],[2,3]],
                #               [[3]]
                #              ]
                # Since nums[i] == nums[i - 1], we don't want to
                # add nums[i] to all subsets i+1,...n since that would
                # give us duplicate subsets.
                #
                # Instead, adding nums[i] to ONLY subsets in dp[i + 1]
                # BECAUSE they are the same would give us new
                # unique subsets. For example:
                #
                # DP:          [
                #               [[2,2],[2,2,3]],
                #               [[2],[2,3]],
                #               [[3]]
                #              ]
                dp[i] = [[nums[i]] + r for r in dp[i + 1]]
            else:
                # newly encounted number, we can add a set of itself
                dp[i].append([nums[i]])
                
                # add this number to every subset that has been found
                # so far to create new subsets
                for j in range(i + 1, n):
                    for subset in dp[j]:
                        dp[i].append([nums[i]] + subset)
                
                # An example of the dp state would look like this:
                # Input:       [1,2,3]
                # i:            0
                # DP:          [
                #               [[1], [1,2],[1,2,3],[1,3]],
                #               [[2],[2,3]],
                #               [[3]]
                #              ]

        # every subset found at every index plus the empty set
        res = [[]]
        for subsets in dp:
            res += subsets
        return res
