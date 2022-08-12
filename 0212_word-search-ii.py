class TrieNode:
    
    def __init__(self, val: str = None, parent: Optional['TrieNode'] = None):
        self.children = {}
        self.val = val
        self.parent = parent
        self.word = None
        

class Trie:
    
    def __init__(self, board: List[List[str]]):
        self.root = TrieNode()
        self.board = board
        self.height = len(self.board)
        self.width = len(self.board[0])
    
    
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(val=c, parent=node)
            node = node.children[c]
        node.word = word


    def searchWord(self,
                   x: int,
                   y: int) -> List[str]:
        """
        Given an (i, j) position on the board, we will perform
        DFS in all four directions (with backtracking) IF
        the new board position allows us to traverse down our Trie.
        
        When a word is found, we will perform the following actions:
        
        - Set the word node's "word" to None

        - If the current word node's child count is 0, we will
          traverse up node's parent and "evict" the child. We will
          perform this check up to trie until we reach a node who's child
          count is not zero OR we are at the root
          
        The reason why we do this is because we only need to match
        a word once. So we will improve subsequent word searches by
        pruning branches to words we've already found. We always check if
        a node's child count is 0 because we don't want to prune
        a branch if there are still words further down.
        
        For example:
            
            "bat", "batter", "battery"
        
        If we found "bat", then "bat" is no longer an eligible word.
        However, "batter" and "battery" are both further down the
        trie, so we don't prune this branch yet.
        
        If we found "battery" next, then this branch would be pruned
        to "bat", "batter".
        
        Finally, after finding "batter", we will prune the entire
        "bat..." branch.
        """
        res = []
        
        trie_node = self.root
        
        seen = set()
        
        def dfs(i, j) -> None:
            nonlocal trie_node
            
            if i < 0 or i == self.height or j < 0 or j == self.width:
                return
            
            if (i, j) in seen:
                return
            
            if self.board[i][j] not in trie_node.children:
                return
            
            # we can use current board position to (maybe) build a word
            seen.add((i, j))
            trie_node = trie_node.children[self.board[i][j]]
            
            if trie_node.word:
                res.append(trie_node.word)
                
                # remove current word from possible match later
                trie_node.word = None
                
                # prune trie until we reach a node with remaining children
                # or the root
                child = trie_node
                parent = child.parent
                while parent and len(child.children) == 0:
                    del parent.children[child.val]
                    child = parent
                    parent = parent.parent

            if len(trie_node.children) == 0:
                # no more words can be built from here
                # no need to dfs further, so we backtrack
                trie_node = trie_node.parent
                seen.remove((i, j))
                return
                    
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
            # back track
            trie_node = trie_node.parent
            seen.remove((i, j))
            
        dfs(x, y)
        
        return res
        
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie(board)
        for word in words:
            trie.addWord(word)
        
        m, n = len(board), len(board[0])
        
        res = []
        
        for i in range(m):
            for j in range(n):
                res.extend(trie.searchWord(i, j))
        
        return res
