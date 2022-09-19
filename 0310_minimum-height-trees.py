# https://leetcode.com/problems/minimum-height-trees/
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            # 2 or fewer nodes, all nodes can be
            # min height trees
            return [i for i in range(n)]
        
        adjacency_list = defaultdict(set)
        for start, end in edges:
            adjacency_list[start].add(end)
            adjacency_list[end].add(start)
            
        # start our BFS with leaf nodes (i.e. nodes
        # with the least amount of edges).
        leaves = deque()
        for i in range(n):
            if len(adjacency_list[i]) == 1:
                leaves.append(i)

        # keep searching until we have 2 or fewer
        # nodes remaining. This means we've found the
        # "center" of the maximum tree diameter (starting
        # from the outer perimeter)
        remaining = n
        while remaining > 2:
            leaf_count = len(leaves)
            remaining -= leaf_count
            
            for _ in range(leaf_count):
                leaf = leaves.popleft()
    
                for neighbor in adjacency_list[leaf]:
                    adjacency_list[neighbor].remove(leaf)
                    if len(adjacency_list[neighbor]) == 1:
                        # neighbor is now a leaf node
                        leaves.append(neighbor)

        # we have 2 or fewer nodes that can be the root of
        # min height trees
        return leaves
            
