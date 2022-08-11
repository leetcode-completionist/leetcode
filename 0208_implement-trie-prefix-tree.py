class TrieNode:
    
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    
    def __searchNode(self, target: str) -> Optional[TrieNode]:
        node = self.root
        for c in target:
            if c not in node.children:
                return None
            node = node.children[c]
        return node
        
        
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True
        

    def search(self, word: str) -> bool:
        node = self.__searchNode(word)
        if not node:
            return False
        return node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        node = self.__searchNode(prefix)
        if not node:
            return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
