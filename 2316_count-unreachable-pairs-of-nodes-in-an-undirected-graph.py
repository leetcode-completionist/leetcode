from typing import Set

class Cluster:
    def __init__(self):
        self.nodes: Set[int] = set()

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency graph
        nodes = {}
        for a, b in edges:
            if a not in nodes and b not in nodes:
                # create new cluster
                cluster = Cluster()
                cluster.nodes.add(a)
                cluster.nodes.add(b)
                nodes[a] = cluster
                nodes[b] = cluster
            elif a not in nodes:
                # add to cluster b
                nodes[b].nodes.add(a)
                nodes[a] = nodes[b]
            elif b not in nodes:
                # add to cluster a
                nodes[a].nodes.add(b)
                nodes[b] = nodes[a]
            elif nodes[a] != nodes[b]:
                # merge
                for node_id in nodes[b].nodes:
                    nodes[a].nodes.add(node_id)
                    nodes[node_id] = nodes[a]
            else:
                # already the same
                nodes[a].nodes.add(b)
                nodes[b].nodes.add(a)
        
        # Array of clusters and count
        cluster_counts = []
        for cluster in set(nodes.values()):
            cluster_counts.append(len(cluster.nodes))
        for i in range(n):
            if i not in nodes:
                # independent node
                cluster_counts.append(1)
        
        # All nodes are reachable from each other.
        cluster_len = len(cluster_counts)
        if cluster_len == 1:
            return 0

        # Create a cache of sums
        cache = [0] * (cluster_len + 1)
        for i in range(cluster_len - 1, -1, -1):
            cache[i] = cluster_counts[i] + cache[i + 1]

        # Calculate number of pairs:
        #
        #   clusters: a, b, c, d
        #
        #   result: len(a) * len(b + c + d)
        #           len(b) * len(c + d)
        #           len(c) * len(d)
        res = 0
        for i in range(cluster_len):
            res += cluster_counts[i] * cache[i + 1]
        return res
