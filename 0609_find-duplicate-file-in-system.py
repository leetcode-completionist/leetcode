# https://leetcode.com/problems/find-duplicate-file-in-system/
import re

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = defaultdict(set)
        
        for path in paths:
            tokens = path.split(" ")
            
            directory = tokens[0]
            
            for token in tokens[1:]:
                s = re.search("^(.+\..+)\((.+)\)", token)
                
                file_path = directory + "/" + s.group(1)
                content = s.group(2)
                
                files[hash(content)].add(file_path)
        
        res = []
        for paths in files.values():
            if len(paths) > 1:
                res.append(list(paths))
        return res
