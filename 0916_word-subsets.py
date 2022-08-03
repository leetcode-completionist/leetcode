from collections import defaultdict

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # keeps track of the minimum freq needed for each char
        freq = defaultdict(lambda: 0)
        for word in words2:
            seen = defaultdict(lambda: 0)
            for c in word:
                seen[c] += 1
            for k, v in seen.items():
                # update freq count to the minimum required
                freq[k] = max(freq[k], v)

        # we will keep track of letters we need to form in order
        # to be considered a universal word
        required = len(freq.keys())
        
        res = []
        for word in words1:
            seen = defaultdict(lambda: 0)
            formed = 0
            for c in word:
                seen[c] += 1
                if c in freq and seen[c] == freq[c]:
                    # increase our formed count as we
                    # newly satisfies a requirement
                    formed += 1
            if formed == required:
                res.append(word)
        return res
