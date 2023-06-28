class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Create a graph of node <-> node with probability
        graph = defaultdict(dict)               
        for (a, b), prob in zip(edges, succProb):
            graph[a][b] = prob
            graph[b][a] = prob
            
        # Keep track of visited nodes with cumulative prob
        seen = {}
        seen[start] = 1
        
        # Use a heap (priority queue) for starting points
        pq = []
        for neighbor, prob in graph[start].items():
            pq.append((-prob, neighbor))
        heapq.heapify(pq)
        
        while pq:
            prob, node = heapq.heappop(pq)
            
            # un-negate it from the max heap
            prob *= -1
            
            if node == end:
                # we reached our end
                # since we use a priority queue, we are guaranteed
                # largest probability
                return prob
            
            if node in seen and seen[node] >= prob:
                # we've been here with a larger prob previously
                continue
                
            seen[node] = prob
            
            # go to all neighbors
            for neighbor, neighbor_prob in graph[node].items():
                heapq.heappush(pq, (-1 * prob * neighbor_prob, neighbor))
        
        # End is unreachable
        return 0.0
        
