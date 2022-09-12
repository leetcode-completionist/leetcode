# https://leetcode.com/problems/additive-number/
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(num: str, target: str, prev: str, seq_count: int) -> bool:
            if not num:
                # reached the end of num, check if we have min sequence count
                return seq_count > 2
            
            # first number in the sequence
            if not target and not prev:
                for i in range(len(num)):
                    if dfs(num[i + 1:], None, num[:i + 1], 1):
                        return True
                    if num[0] == "0":
                        # no nums with leading "0"
                        # so we stop with one iteration
                        break
                return False
            
            # second number in the sequence
            if not target:
                for i in range(len(num)):
                    cand = num[:i + 1]
                    target = str(int(prev) + int(cand))    
                    if dfs(num[i + 1:], target, cand, 2):
                        return True
                    if num[0] == "0":
                        # no nums with leading "0"
                        # so we stop with one iteration
                        break
                return False
            
            if num[:len(target)] != target:
                # target not found in beginning of num
                return False
            
            return dfs(num[len(target):],
                       str(int(target) + int(prev)),    # new target
                       target,                          # prev
                       seq_count + 1)

        return dfs(num, None, None, 0)
