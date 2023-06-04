from typing import List, Tuple

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        groups = {}
        
        for i in range(n):
            groups[i] = i        
        
        def find(city: int) -> int:
            node = groups[city]
            while node != groups[node]:
                node = groups[node]
            return node
        
        def union(src: int, dst: int) -> int:
            src_root = find(src)
            dst_root = find(dst)
            
            if src_root == dst_root:
                return dst_root
            
            groups[src_root] = dst_root
            
            return dst_root
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j]:
                    union(i, j)
                    
        res = set()
        for i in range(n):
            province = find(i)
            res.add(province)
        
        return len(res)
