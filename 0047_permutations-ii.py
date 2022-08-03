class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def dfs(nums: List[int], permutation: List[int]) -> List[List[int]]:
            if not nums:
                return [permutation]
            
            res = []
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                n_nums = nums[:i] + nums[i+1:]
                n_permutation = permutation[:]
                n_permutation.append(nums[i])
                
                res.extend(dfs(n_nums, n_permutation))
            return res
        
        return dfs(nums, [])
