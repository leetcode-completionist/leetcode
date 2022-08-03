class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            m = {}
            for w, p in zip(word, pattern):
                if w in m:
                    if m[w] != p:
                        # we previously mapped this to a different char
                        # no longer a match!
                        return False
                else:
                    m[w] = p
            # every char in word is matched to a different char in pattern
            return len(m.values()) == len(set(m.values()))
        
        res = []
        for word in words:
            if match(word):
                res.append(word)
        return res
