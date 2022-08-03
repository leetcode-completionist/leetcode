class Solution:
    
    LETTERS = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        
        # Initialize with first digit
        res.extend(Solution.LETTERS[digits[0]])
        
        for digit in digits[1:]:
            n_res = []
            for combo in res:
                for letter in Solution.LETTERS[digit]:
                    n_res.append(combo + letter)
            res = n_res
            
        return res
