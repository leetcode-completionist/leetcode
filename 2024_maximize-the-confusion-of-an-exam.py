class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """
        Intuition
        
        Keep a sliding window of consecutive letters with at most k "flips"
        Return the max size of sliding window seen.

        How do we know how many "flips" we need to maintain a valid sliding window?
        Since we only have two letters, we always want to flip the minority.
        
        So "flips" will be min('T' count, 'F' count).        
        """
        
        res = k
        counter = Counter(answerKey[:k])
            
        left = 0
        for right in range(k, len(answerKey)):   
            counter[answerKey[right]] += 1
            
            while min(counter["T"], counter["F"]) > k:
                counter[answerKey[left]] -= 1
                left += 1
                
            res = max(res, right - left + 1)
        
        return res
