class Node:
    
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True
        

    def search(self, word: str) -> bool:
        q = deque([self.root])
        for c in word:
            if not q:
                return False
            
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if c == ".":
                    q.extend(node.children.values())
                elif c in node.children:
                    q.append(node.children[c])
        
        return any(node.is_word for node in q)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
