class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        
        n = len(arr)
        
        trees = defaultdict(lambda: 0)
        
        for i in range(n):
            num = arr[i]
            
            count = 0
            for j in range(i):
                factor_1 = arr[j]
                if num % factor_1 == 0:
                    factor_2 = num // factor_1
                    if factor_1 in trees and factor_2 in trees:
                        count += (trees[factor_1] * trees[factor_2]) % (10**9 + 7)

            trees[num] += 1 + count
        
        return sum(trees.values()) % (10**9 + 7)
