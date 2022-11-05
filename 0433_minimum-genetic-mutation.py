# https://leetcode.com/problems/minimum-genetic-mutation/
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        
        # map pattern to genes
        pattern_to_gene = defaultdict(set)
        for gene in bank:
            for i in range(len(gene)):
                pattern = gene[:i] + "#" + gene[i + 1:]
                pattern_to_gene[pattern].add(gene)
        
        # initialize BFS queue
        q = deque([startGene])
        visited = set([startGene])
        
        res = 0
        
        while q:
            q_len = len(q)
            for _ in range(q_len):
                gene = q.popleft()
                
                visited.add(gene)
                
                if gene == endGene:
                    return res
        
                for i in range(len(gene)):
                    pattern = gene[:i] + "#" + gene[i + 1:]
                    nextGenes = pattern_to_gene[pattern]
                    
                    for nextGene in nextGenes:
                        if nextGene not in visited:
                            q.append(nextGene)
            res += 1
            
        # exhausted all conversions, not possible
        return -1
