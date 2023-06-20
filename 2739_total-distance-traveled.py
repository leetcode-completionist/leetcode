class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        d = 0
        
        inject = 0
        while mainTank:
            mainTank -= 1
            inject += 1
            d += 10
            
            if inject == 5 and additionalTank:
                mainTank += 1
                additionalTank -= 1
                inject = 0
        
        return d
