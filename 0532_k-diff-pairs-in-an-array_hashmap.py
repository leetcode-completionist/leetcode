class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        res = 0
        for num, freq in counter.items():
            if k == 0:
                # edge case
                if freq > 1:
                    # pair of the numbers
                    # with equal value
                    res += 1
            elif (num + k) in counter:
                # only look forward to avoid dup pairs
                res += 1
        return res
