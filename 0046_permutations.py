class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums: List[int], permutation: List[int]) -> List[List[int]]:
            # we have used every nums, return the permutation
            if not nums:
                return [permutation]
            
            res = []
            for i in range(len(nums)):
                # use current number and take it out of nums for the
                # next recursive call
                n_nums = nums[:i] + nums[i+1:]
                
                # add current number to the permutation
                n_permutation = permutation[:]
                n_permutation.append(nums[i])
                
                res.extend(dfs(n_nums, n_permutation))
            return res
        
        return dfs(nums, [])
