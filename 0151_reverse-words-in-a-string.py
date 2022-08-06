class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words = list(filter(lambda x: len(x.strip()) > 0, words))
        return " ".join(words[::-1])
