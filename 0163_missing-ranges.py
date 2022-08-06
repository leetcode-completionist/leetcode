class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # start our missing at the lower bound
        missing = lower
        
        res = []
        
        for num in nums:
            if num > missing:
                # we have a new range
                if missing == num - 1:
                    res.append(str(missing))
                else:
                    res.append("{}->{}".format(missing, num - 1))
                missing = num + 1

            elif missing == num:
                # move missing to the next number
                missing += 1

            else:
                raise Exception("illegal test input: {}".format(nums))
        
        # are we missing anything from last seen to upper?
        if missing <= upper:
            if missing == upper:
                res.append(str(missing))
            else:
                res.append("{}->{}".format(missing, upper))
        
        return res
