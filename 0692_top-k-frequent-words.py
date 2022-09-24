# https://leetcode.com/problems/top-k-frequent-words/
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # count words
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        # create heap nodes in linear time
        heap = []
        for word, count in word_count.items():
            heap.append((-count, word))
        
        # heapify in linear time
        heapq.heapify(heap)
        
        # grab top k words in O(k * log2(n)) time
        res = []
        while heap and k:
            _, word = heapq.heappop(heap)
            res.append(word)
            k -= 1
            
        return res
