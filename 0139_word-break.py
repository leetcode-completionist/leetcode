class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:        
        # build a word trie for a scalable way of storing and
        # searching a list of words
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)
        
        n = len(s)
        dp = [False] * n
        
        # initialize with a True at n+1 for empty string base case
        dp.append(True) 
        
        for i in range(n - 1, -1, -1):
            # at every index, traverse trie
            node = trie.root
            
            # for substring starting at i
            for j in range(i, n):
                child = node.getChild(s[j])
                
                # we will either break out because we can't build any words
                if not child:
                    break
                
                # Or create a word at s[i:j] and look up whether or not s[j:]
                # is a valid word break
                if child.is_word and dp[j + 1] == True:
                    dp[i] = True
                    
                    # We can break out optimistically here
                    # since we already know s[i:] is a valid word break
                    break
                
                # Or in the process of building a word
                node = child
        
        return dp[0]

        
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
