class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # build a word trie for a scalable way of storing and
        # searching a list of words
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)
        
        # initialize DP
        n = len(s)
        dp = []
        for i in range(n):
            dp.append([])
        
        # initialize an empty array at n+1 for empty string base case
        dp.append([[]])
        
        for i in range(n - 1, -1, -1):
            # at every index, traverse trie
            node = trie.root
            
            # for substring starting at i
            for j in range(i, n):
                child = node.getChild(s[j])
                
                # we will either break out because we can't build any words
                if not child:
                    break
                
                # Or create a word at s[i:j+1] with possible word breaks in
                # s[j+1:]
                if child.is_word:
                    for wl in dp[j + 1]:
                        dp[i].append([s[i : j + 1]] + wl)
                    
                    # we cannot break out yet because we need to find
                    # ALL possible word breaks
                
                # continue to build possible word
                node = child
        
        # format the results
        res = []
        for r in dp[0]:
            res.append(" ".join(r))
        return res

        
class TrieNode:
    def __init__(self, val: str):
        self.val = val
        self.children = {}
        self.is_word = False

    
    def add(self, c: str) -> 'TrieNode':
        if c not in self.children:
            self.children[c] = TrieNode(c)
        return self.children[c]
    
    
    def getChild(self, c: str) -> Optional['TrieNode']:
        if c not in self.children:
            return None
        return self.children[c]

        
class Trie:
    def __init__(self):
        self.root = TrieNode(val=None)
        

    def addWord(self, word: str):
        node = self.root
        for c in word:
            node = node.add(c)
        node.is_word = True
