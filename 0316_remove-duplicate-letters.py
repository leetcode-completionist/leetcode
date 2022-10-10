# https://leetcode.com/problems/remove-duplicate-letters/
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        res = []

        seen = set()

        for c in s:
            freq[c] -= 1

            if c in seen:
                continue

            while res and res[-1] > c and freq[res[-1]] > 0:
                n = res.pop()
                seen.remove(n)

            res.append(c)
            seen.add(c)

        return "".join(res)
