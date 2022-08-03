class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for s in strs:
            # freq array
            freq = [0]*26
            for c in s:
                freq[ord(c)-ord('a')] += 1
            
            # make it a tuple so it is immutable
            # and can be used as a dict key
            k = tuple(freq)
            if k not in anagrams:
                anagrams[k] = []
            anagrams[k].append(s)
            
        return anagrams.values()
