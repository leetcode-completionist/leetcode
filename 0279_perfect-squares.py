# https://leetcode.com/problems/perfect-squares/
class Solution:
    def numSquares(self, n: int) -> int:
        res = 0

        q = deque([n])

        while q:
            res += 1

            len_q = len(q)
            for _ in range(len_q):
                num = q.popleft()
        
                if num == 0:
                    return res
        
                # first find the max perfect square we can start with
                max_square = int(math.floor(math.sqrt(num)))

                for i in range(max_square, 0, -1):
                    # try out each square between [1, max_square]
                    next_num = num - i ** 2
                    
                    # we managed to get to zero in our BFS
                    # return our results
                    if next_num == 0:
                        return res
                    else:
                        # we haven't reached zero yet, keep
                        # going
                        q.append(next_num)
            
        raise Exception("we should always be able to find the answer")
