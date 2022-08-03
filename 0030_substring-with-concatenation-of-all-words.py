class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 1. preprocessing
        trie = TrieNode()
        req = {}
        total_char_count = 0
        for word in words:
            # build trie
            node = trie
            for c in word:
                node = node.add(c)
            node.word = word
            
            # build requirements
            if word not in req:
                req[word] = 0
            req[word] += 1
        
            # track total char count
            total_char_count += len(word)
            
        # 2. sliding window of size total_char_count
        res = []
        for i in range(len(s) - total_char_count + 1):
            seen = {}
            node = trie

            for c in s[i:i + total_char_count]:
                node = node.get(c)
                if not node:
                    # invalid sliding window
                    break
                
                if node.word:
                    # we encountered a word_node
                    if node.word not in seen:
                        seen[node.word] = 0
                    seen[node.word] += 1
                    
                    if seen[node.word] > req[node.word]:
                        # invalid sliding window
                        break
                        
                    # We assume words can't be subwords of each other
                    # so after we encounter a word, we go back to trie
                    # root node.
                    # 
                    # If we allow subwords, then we need a queue of 
                    # possible nodes to check per char of the sliding window
                    node = trie
            
            # check if substring satisfies requirements
            valid = True
            for k, v in req.items():
                if k not in seen:
                    valid = False
                    break
                if seen[k] != v:
                    valid = False
                    break
            
            if valid:
                res.append(i)
        
        return res
                

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = ""
        
    def add(self, c: str):
        i = ord(c) - ord("a")
        if not self.children[i]:
            self.children[i] = TrieNode()
        return self.children[i]
    
    def get(self, c: str):
        i = ord(c) - ord("a")
        if not self.children[i]:
            return None
        return self.children[i]
