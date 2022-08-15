# https://leetcode.com/problems/shortest-word-distance-iii/
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        indices_map = defaultdict(list)
        for i, word in enumerate(wordsDict):
            indices_map[word].append(i)
            
        if word1 == word2:
            return self.shortestSame(indices_map[word1])
        else:
            return self.shortestDifferent(indices_map[word1], indices_map[word2])
    
    
    def shortestSame(self, indices: List[int]) -> int:
        res = math.inf
        for i in range(1, len(indices)):
            res = min(res, abs(indices[i] - indices[i - 1]))
        return res
    
    
    def shortestDifferent(self, indices1: List[int], indices2: List[int]) -> int:
        res = math.inf
        
        i, j = 0, 0
        while i < len(indices1) and j < len(indices2):
            index1 = indices1[i]
            index2 = indices2[j]
            
            res = min(res, abs(index1 - index2))
            if index1 < index2:
                i += 1
            else:
                j += 1
        
        return res
