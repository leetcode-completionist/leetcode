class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        q = deque(sorted(people))
        res = 0
        while q:
            weight = q.pop()
            if q and q[0] <= (limit - weight):
                q.popleft()
            res += 1
        return res
