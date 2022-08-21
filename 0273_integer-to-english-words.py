# https://leetcode.com/problems/integer-to-english-words/
class Solution:
    
    ZERO = "Zero"
    
    ONES = [
        None, "One", "Two", "Three",
        "Four", "Five", "Six", "Seven",
        "Eight", "Nine",
    ]
    
    TEN_TO_NINETEEN = [
        "Ten", "Eleven", "Twelve", "Thirteen",
        "Fourteen", "Fifteen", "Sixteen", "Seventeen",
        "Eighteen", "Nineteen",
    ]
    
    TENS = [
        None, None, "Twenty", "Thirty",
        "Forty", "Fifty", "Sixty", "Seventy",
        "Eighty", "Ninety"
    ]
    
    HUNDRED = "Hundred"
    
    THOUSAND = "Thousand"
    
    MILLION = "Million"
    
    BILLION = "Billion"
    
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return Solution.ZERO
        
        def getWords(num: int) -> List[str]:
            if num == 0:
                return []
            
            if num < 10:
                return [Solution.ONES[num]]

            if num < 20:
                return [Solution.TEN_TO_NINETEEN[num % 10]]

            if num < 100:
                words = []
                if num % 10 != 0:
                    words.append(Solution.ONES[num % 10])
                
                num //= 10
                words = [Solution.TENS[num % 10]] + words
                return words

            if num < 1_000:
                words = getWords(num % 100)
                num //=100
                words = [Solution.ONES[num % 10], Solution.HUNDRED] + words
                return words
            
            if num < 1_000_000:
                words = getWords(num % 1_000)
                num //= 1_000
                words = getWords(num) + [Solution.THOUSAND] + words
                return words
        
            if num < 1_000_000_000:
                words = getWords(num % 1_000_000)
                num //= 1_000_000
                words = getWords(num) + [Solution.MILLION] + words
                return words
            
            else:
                # max is 2^31-1 (i.e. 2 billion....)
                words = getWords(num % 1_000_000_000)
                num //= 1_000_000_000
                words = getWords(num) + [Solution.BILLION] + words
                return words
        
        return " ".join(getWords(num))
