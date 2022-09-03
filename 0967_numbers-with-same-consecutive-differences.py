# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        
        def getNums(i: int, num: int) -> None:
            if i == n:
                # we reached our required number of digits
                # add to results
                res.append(num)
                return num

            last_digit = num % 10
            
            # we use a set because we might end up with same number
            # after +/- k
            next_digits = set([last_digit + k, last_digit - k])
            
            for digit in next_digits:
                if 0 <= digit <= 9:
                    # digit is valid, get the next digit
                    getNums(i + 1, num * 10 + digit)

        # first digit cannot be a zero
        for i in range(1, 10):
            getNums(1, i)
        
        return res
