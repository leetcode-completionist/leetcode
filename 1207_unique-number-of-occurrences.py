# https://leetcode.com/problems/unique-number-of-occurrences/
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = defaultdict(int)
        for n in arr:
            occurrences[n] += 1
        
        all_occurrences = occurrences.values()
        
        return len(all_occurrences) == len(set(all_occurrences))
