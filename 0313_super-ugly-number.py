# https://leetcode.com/problems/super-ugly-number/
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = primes[:]
        heapq.heapify(nums)
        
        res = 1
        for i in range(n - 1):
            res = heapq.heappop(nums)
            
            for prime in primes:
                heapq.heappush(nums, res * prime)
                
                if res % prime == 0:
                    break
        return res
