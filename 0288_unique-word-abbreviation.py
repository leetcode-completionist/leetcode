# https://leetcode.com/problems/unique-word-abbreviation/
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbreviations = defaultdict(set)
        
        for word in dictionary:
            abbreviation = self.__abbreviate__(word)
            self.abbreviations[abbreviation].add(word)
            
        
    def __abbreviate__(self, word: str) -> str:
        if len(word) <= 2:
            return word
        
        return word[0] + str(len(word) - 2) + word[-1]
    
        
    def isUnique(self, word: str) -> bool:
        abbreviation = self.__abbreviate__(word)
        
        if abbreviation not in self.abbreviations:
            return True
        
        words = self.abbreviations[abbreviation]
        if len(words) > 1:
            return False
        
        return word in words
        

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
