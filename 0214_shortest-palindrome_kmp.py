class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        Given a string (e.g. "abab"). We will perform the
        following actions:
        
        1. Create a reversed s (i.e. "baba")
        
        2. Determine the longest prefix in "abab" that matches the
           longest suffix "baba". In this case, that is "aba".
           
        3. We will remove the longest prefix "baba" which leaves us
           with only "b"
           
        4. Then we will use "b" as the prefix and append the original
           string "abab", giving us "babab"
           
        In order to perform step #2 efficiently (i.e. O(n)), we will use
        the Knuth-Morris-Pratt (KMP) Pattern Matching Algorithm.
        
        But we will ONLY use the prefix lookup table. This table tells us
        the longest prefix that reappears at the later part of the string.
        """
        if s == s[::-1]:
            # already a palindrome
            return s
        
        # first reverse the input
        rev = s[::-1]
        
        # add it to the end of the input for a guaranteed palindrome
        # we add a delimiter to prevent KMP from matching a prefix that
        # spans beyond the initial input
        pattern = s + "#" + rev
        
        # but we want to see how many letters we can remove from rev
        # to minimize our transformation.
        #
        # to do this, we create the KMP prefix lookup table.
        prefix_arr = self.kmp(pattern)
        
        # maximum length of matched at the last character
        l = prefix_arr[-1]
        
        # remove the first l elements from s
        # then we reverse the output to be added to the output
        new_characters = s[l:][::-1]
        
        return new_characters + s
        
        
    def kmp(self, pattern: str) -> List[int]:
        n = len(pattern)

        kmp = [-1] * (n + 1)
        
        # i will be moved forward across every letter in the pattern
        i = 0
        
        # j will be move as we match letters from the beginning of
        # the pattern to letters being iterated.
        #
        # if we ever get a mismatch, we reset j back to the front
        j = -1
        
        while i < n:
            
            while j > -1 and pattern[j] != pattern[i]:
                # we no longer match, jump back and try to match again
                j = kmp[j]

            i += 1
            j += 1
            
            # set the current kmp value to max match
            kmp[i] = j
            
        return kmp
