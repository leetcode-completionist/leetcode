# https://leetcode.com/problems/alien-dictionary/
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # compare words in pairs to build up adjacency list
        out_degree = defaultdict(set)
        in_degree = defaultdict(set)
        
        # unique set of all chars
        unique = set([*words[0]])
        
        # compare words in pairs (i.e. before vs. after)
        wordBefore = words[0]
        for i in range(1, len(words)):
            wordAfter = words[i]
            
            # build up a set of unique chars
            for c in wordAfter:
                unique.add(c)
            
            # compare each letter until we come
            # across a difference
            for j in range(len(wordBefore)):
                if j == len(wordAfter):
                    # the original words are NOT in
                    # lexicographical ordering
                    return ""
                
                if wordBefore[j] != wordAfter[j]:
                    out_degree[wordBefore[j]].add(wordAfter[j])
                    in_degree[wordAfter[j]].add(wordBefore[j])
                    # we break immediately because we
                    # won't know the lexicographic ordering
                    # after this letter
                    break
            
            # current word becomes wordBefore
            # and will be used to compare with the next word
            wordBefore = wordAfter
        
        res = ""
        visited = set()
        
        # start off a BFS with characters without any in-degrees
        q = deque(filter(lambda c: c not in in_degree, unique))
        while q:
            n = len(q)
            
            for _ in range(n):
                c = q.popleft()
                if c in visited:
                    # loop detected, invalid alien dictionary
                    return ""
                
                visited.add(c)
                res += c
                
                # attempt to add next chars to BFS queue
                for out in out_degree[c]:
                    if out in in_degree:
                        # remove requirement
                        in_degree[out].remove(c)
                        
                    if out not in in_degree or not in_degree[out]:
                        # if no more requirement
                        # queue up char for BFS
                        q.append(out)
        
        # return the result iff it contains all unique chars        
        return res if len(res) == len(unique) else ""
