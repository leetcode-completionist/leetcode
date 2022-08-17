# https://leetcode.com/problems/graph-valid-tree/
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:      
        adjacency_lists = defaultdict(list)
        for node_a, node_b in edges:
            adjacency_lists[node_a].append(node_b)
            adjacency_lists[node_b].append(node_a)

        # keeps track of all nodes we have visited
        seen = set()
        
        # keeps track of nodes we saw at the last level of BFS
        prev = set()
        
        q = deque([0])

        while q:
            # keeps track of nodes we see at this level of BFS
            n_prev = set()
            for _ in range(len(q)):
                node = q.popleft()
                
                if node in seen:
                    # cycle detected
                    return False
                
                seen.add(node)
                n_prev.add(node)
                
                # prevent us from going back to previous nodes
                next_nodes = list(filter(
                        lambda next_node: next_node not in prev,
                        adjacency_lists[node]))
                
                q.extend(next_nodes)
            
            # update prev nodes to all nodes seen at this level
            prev = n_prev
            
        # valid only if we've visited every nodes from a single node
        return len(seen) == n
