# https://leetcode.com/problems/satisfiability-of-equality-equations/
class Equality:
    def __init__(self):
        self.parent = {}
        self.children = defaultdict(set)
    
    
    def isEqual(self, a: str, b: str) -> bool:
        if a not in self.parent or b not in self.parent:
            return False
        return self.parent[a] == self.parent[b]
    
    
    def add(self, a: str, b: str) -> None:
        if a not in self.parent:
            self.parent[a] = a
            self.children[a].add(a)
        if b not in self.parent:
            self.parent[b] = b
            self.children[b].add(b)

        small, big = self.parent[a], self.parent[b]
        if small == big:
            return
        
        if len(self.children[small]) > len(self.children[big]):
            small, big = big, small
                
        for child in self.children[small]:
            self.parent[child] = big
            self.children[big].add(child)
            
        del self.children[small]

        
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equality = Equality()
        
        for equation in equations:
            if equation[1:3] == "==":
                equality.add(equation[0], equation[3])
                
        for equation in equations:
            if equation[1:3] == "!=":
                if equation[0] == equation[3] or equality.isEqual(equation[0], equation[3]):
                    return False
            
        return True
        
