# https://leetcode.com/problems/palindrome-permutation-ii/
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
            
        odd = None
        for k in freq.keys():
            if freq[k] % 2 != 0:
                if odd:
                    # more than one char with odd occurrences,
                    # not a valid palindrome permitation
                    return []
                odd = k
                
            # divide everything in half
            # since we only need to generate
            # half of a palindrome
            freq[k] //= 2
        
        # generate an initial array of occurring characters
        chars = []
        for k, v in freq.items():
            chars += [k] * v
            
        # generate all permutations
        permutations = self.dfs(chars, [])
        
        # create full palindromes
        res = []
        for permutation in permutations:
            if odd:
                permutation += [odd] + permutation[::-1]
            else:
                permutation += permutation[::-1]
            res.append("".join(permutation))

        return res
    
    
    def dfs(self, chars: List[str], permutation: List[str]) -> List[List[str]]:
            if not chars:
                return [permutation]
            
            res = []
            for i in range(len(chars)):
                if i > 0 and chars[i] == chars[i-1]:
                    # skip the same number to reduce duplicates
                    continue
                n_chars = chars[:i] + chars[i+1:]
                n_permutation = permutation[:]
                n_permutation.append(chars[i])
                
                res.extend(self.dfs(n_chars, n_permutation))
            return res
