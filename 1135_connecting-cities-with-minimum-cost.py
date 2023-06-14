import heapq

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        edges = defaultdict(list)
        for src, dst, cost in connections:
            edges[src].append((dst, cost))
            edges[dst].append((src, cost))
        
        visited = set()       
        frontier = [(0, 1)]
        res = 0
        
        while frontier:
            cost, dst = heapq.heappop(frontier)
            if dst in visited:
                continue
            visited.add(dst)
            res += cost
            
            for next_dst, cost in edges[dst]:
                if next_dst not in visited:
                    heapq.heappush(frontier, (cost, next_dst))
                
        if len(visited) != n:
            return -1
        
        return res
