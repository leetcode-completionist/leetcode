class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        
        for i, flower in enumerate(flowerbed):
            if flower:
                continue

            empty_left = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
            
            if empty_left and empty_right:
                count += 1
                flowerbed[i] = 1
        
        return count >= n
