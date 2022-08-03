class Solution:
    
    WILDCARD = "."
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adjacency_list = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + Solution.WILDCARD + word[i+1:]
                adjacency_list[pattern].append(word)
                
        count = 1
        visited = set([beginWord])
        q = deque([beginWord])
        while q:
            n = len(q)
            visited_this_level = set()
            for _ in range(n):
                word = q.popleft()
                for i in range(len(word)):
                    pattern = word[:i] + Solution.WILDCARD + word[i+1:]
                    for next_word in adjacency_list[pattern]:
                        if next_word == endWord:
                            return count + 1
                        if next_word not in visited:
                            if next_word not in visited_this_level:
                                q.append(next_word)
                            visited_this_level.add(next_word)
                            
            visited.update(visited_this_level)
            count += 1
        
        return 0
