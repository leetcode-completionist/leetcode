class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        if not questions:
            return 0
        
        n = len(questions)
        
        @cache
        def dp(i: int) -> int:
            if i >= n:
                return 0
            if i == (n - 1):
                return questions[i][0]
            
            return max(
                questions[i][0] + dp(i + questions[i][1] + 1),
                dp(i + 1)
            )
        
        return dp(0)
