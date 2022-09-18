# https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_idx = {}
        for i, c in enumerate(order):
            order_idx[c] = i
            
        for i in range(1, len(words)):
            before = words[i - 1]
            current = words[i]
            
            j, k, is_sorted = 0, 0, False
            while j < len(before) and k < len(current):
                if before[j] == current[k]:
                    j += 1
                    k += 1
                elif order_idx[before[j]] > order_idx[current[k]]:
                    return False
                else:
                    is_sorted = True
                    break
            
            if not is_sorted and len(before) > len(current):
                return False
        
        return True
