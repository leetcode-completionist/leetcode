class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        We can pretend we have infinite rooms stacked vertically
        the ray is allowed to pass through the ceiling but will
        continue to bounce left-right until it hits a receptor
        
        Each room will be height of "p"
        
        In order for the ray to hit a receptor, we find the least
        common multiple of p and q.
        
        For example, a room of p: 4 and q: 2 will have the ray to reach
        a receptor after one reflection. A room of p: 4 and q: 3 will
        require 3 rooms for a total height of 12.
        
        Next we count the number of reflections required: lcm // q

        Next we count the number of rooms required: lcm // p
        """
        
        lcm = math.lcm(p, q)
        
        if (lcm // q) % 2 == 0:
            # number of reflections required are even
            # so we will always land on the receptor at the
            # left-hand side
            return 2
        
        # if room is odd, then we are looking at receptor 1
        if (lcm // p) % 2 == 1:
            return 1
        
        # else we are looking at receptor 0
        # 
        # this is because in the first room, if we hit the top
        # right corner, that will be receptor 1.
        #
        # in the next room, if we hit the top right corner again,
        # we are actually reflecting off the mirrors onto receptor
        # 0.
        return 0
