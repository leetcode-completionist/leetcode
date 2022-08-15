# https://leetcode.com/problems/shortest-word-distance-ii/
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.indices = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.indices[word].append(i)

            
    def shortest(self, word1: str, word2: str) -> int:
        indices1 = self.indices[word1]
        indices2 = self.indices[word2]
        
        res = math.inf
        
        i, j = 0, 0
        while i < len(indices1) and j < len(indices2):
            index1 = indices1[i]
            index2 = indices2[j]
            
            res = min(res, abs(index1 - index2))
            
            if index1 < index2:
                i += 1
            else:
                # index2 > index1
                # we don't have to worry about index2 == index1
                # because the problem guarantees that
                # word1 and word2 are different
                j += 1
        
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
