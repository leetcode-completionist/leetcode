# https://leetcode.com/problems/strobogrammatic-number-iii/
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        int_low = int(low)
        int_high = int(high)
        
        low_n = len(low)
        high_n = len(high)
        
        def find(i: int, n: int) -> List[str]:
            if i == 1:
                nums = ["0", "1", "8"]
                if low_n == 1:
                    nums = filter(lambda num: num >= low, nums)
                if high_n == 1:
                    nums = filter(lambda num: num <= high, nums)
                return list(nums)
            
            if i == 2:
                nums = ["00", "11", "69", "88", "96"]
                if n == 2:
                    # we don't use zeroes at the top level
                    nums = nums[1:]
                if low_n == 2:
                    nums = filter(lambda num: int(num) >= int_low, nums)
                if high_n == 2:
                    nums = filter(lambda num: int(num) <= int_high, nums)
                return list(nums)

            res = []
            
            pairs = ["00", "11", "69", "88", "96"]
            if i == n:
                # we don't use zeroes at the top level
                pairs = pairs[1:]
            
            middle = find(i - 2, n)
            
            too_large = False
            for pair in pairs:
                if too_large:
                    # break out early to save unnecessary computations
                    break
                
                for s in middle:
                    num = pair[0] + s + pair[1]
                    
                    int_num = int(num)
                    
                    if high_n == i and int_num > int_high:
                        # break out early because all subsequent
                        # nums will be too high
                        too_large = True
                        break
                    if low_n == i and int_num < int_low:
                        continue

                    res.append(num)
            
            return res
        
        res = []
        
        for n in range(low_n, high_n + 1):
            res += find(n, n)
        
        return len(res)
