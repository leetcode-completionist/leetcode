class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        # Build adjacency graph
        adjacent_nodes: Dict[int] = {}
        for i, node in enumerate(edges):
            adjacent_nodes[i] = node
        
        # Keep a stack of nodes visited
        stack: List[int] = []
        stack_idx: Dict[int] = {}
        
        # Keep track of nodes that belongs to a cycle.
        nodes_in_cycle: Set[int] = set()
            
        res = -1
                
        def dfs(node: int) -> None:
            nonlocal stack, res
            
            if node == -1:
                # No outgoing node
                return
            
            if node in nodes_in_cycle:
                # We already went into this cycle
                return
            
            if node not in stack_idx:
                # Keep track of node seen in current branch
                stack.append(node)
                stack_idx[node] = len(stack) - 1
                
                dfs(adjacent_nodes[node])
                
                # Backtrack
                if node in stack_idx:
                    stack.pop()
                    del stack_idx[node]
                
            else:          
                # We are in a cycle
                idx = stack_idx[node]
                cycle = stack[idx:]
                                
                # Update longest cycle seen so far
                res = max(res, len(cycle))

                # Keep track of nodes in cycle
                for node in cycle:
                    nodes_in_cycle.add(node)
                
                # Pop cycle from visited
                stack = stack[:idx]
                for node in cycle:
                    del stack_idx[node]

        # For each untraversed node, DFS
        for k in adjacent_nodes.keys():
            if k in stack:
                continue
            dfs(k)
        
        # At the end of DFS, return the longest cycle
        # we've seen.
        return res
