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
                    nums = list(filter(lambda num: num >= low, nums))
                if high_n == 1:
                    nums = list(filter(lambda num: num <= high, nums))
                return nums
            
            if i == 2:
                nums = ["00", "11", "69", "88", "96"]
                if n == 2:
                    # we don't use zeroes at the top level
                    nums = nums[1:]
                if low_n == 2:
                    nums = list(filter(lambda num: int(num) >= int_low, nums))
                if high_n == 2:
                    nums = list(filter(lambda num: int(num) <= int_high, nums))
                return nums

            res = []
            
            pairs = ["00", "11", "69", "88", "96"]
            if n == i:
                # we don't use zeroes at the top level
                pairs = pairs[1:]
            if low_n == i:
                pairs = list(filter(lambda num: num[0] >= low[0], pairs))
            if high_n == i:
                pairs = list(filter(lambda num: num[0] <= high[0], pairs))
            
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
        
        res = 0
        
        for n in range(low_n, high_n + 1):
            res += len(find(n, n))
        
        return res
