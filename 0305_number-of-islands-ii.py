# https://leetcode.com/problems/number-of-islands-ii/
class Islands:
    def __init__(self):
        self.parents = {}
        self.children = {}
        
    
    def addIsland(self, pos: Tuple[int]) -> None:
        # initialize the island
        self.parents[pos] = pos
        self.children[pos] = set([pos])
        
        # merge with top
        if (top := (pos[0] - 1, pos[1])) in self.parents:
            self.mergeIslands(top, pos)
        
        # merge with left
        if (left := (pos[0], pos[1] - 1)) in self.parents:
            self.mergeIslands(left, pos)
        
        # merge with bottom
        if (bottom := (pos[0] + 1, pos[1])) in self.parents:
            self.mergeIslands(bottom, pos)
        
        # merge with right
        if (right := (pos[0], pos[1] + 1)) in self.parents:
            self.mergeIslands(right, pos)
    
    
    def mergeIslands(self, pos1: Tuple[int], pos2: Tuple[int]) -> None:        
        small = self.parents[pos1]
        large = self.parents[pos2]
        
        if small == large:
            # no need to merge
            return
        
        # 1. determine which island is larger
        if len(self.children[small]) > len(self.children[large]):
            small, large = large, small

        # 2. merge the smaller island into larger island
        for pos in self.children[small]:
            self.parents[pos] = large
            self.children[large].add(pos)
            
        # 3. clean up children from the prev small island
        del self.children[small]
            
    
    def count(self) -> int:
        return len(self.children.keys())
        
        
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res = []
        islands = Islands()
        for pos in positions:
            pos = tuple(pos)
            islands.addIsland(pos)
            res.append(islands.count())
        return res
