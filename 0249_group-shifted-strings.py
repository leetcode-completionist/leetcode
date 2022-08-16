# https://leetcode.com/problems/group-shifted-strings/
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strings:
            offset = ord(s[0]) - ord("a") - 1
            
            arr = []
            for c in s:
                i = ord(c) - ord("a") - offset
                if i <= 0:
                    i += 26
                arr.append(i)

            groups[tuple(arr)].append(s)
        
        return groups.values()
