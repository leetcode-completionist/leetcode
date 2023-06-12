class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counter = defaultdict(int)
        for i in range(0, len(s) - minSize + 1):
            if len(Counter(s[i:i + minSize])) <= maxLetters:
                counter[s[i:i + minSize]] += 1   
        return max(counter.values(), default=0)
