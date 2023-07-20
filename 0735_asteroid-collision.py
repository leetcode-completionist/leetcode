class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        
        def willCollide(a: int, b: int) -> bool:
            return a > 0 and b < 0
        
        for a in asteroids:
            if not res:
                res.append(a)
                continue
                
            if not willCollide(res[-1], a):
                res.append(a)
                continue
                
            exploded = False
            
            while res and willCollide(res[-1], a) and not exploded:
                prev = abs(res[-1])
                cur = abs(a)
                
                if prev > cur:
                    # current asteroid will explode
                    exploded = True
                    break
                elif prev == cur:
                    # both will explose
                    res.pop()
                    exploded = True
                else:
                    # prev asteroid will explode
                    res.pop()
                
            if not exploded:
                # no further collisions
                res.append(a)
                
        return res
