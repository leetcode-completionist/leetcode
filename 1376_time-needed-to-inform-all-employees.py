from collections import defaultdict, deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, managers: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        
        for employee, manager in enumerate(managers):
            if manager == -1:
                continue
            graph[manager].append(employee)
        
        q = deque([(headID, 0)])
        
        res = 0
        
        while q:
            n = len(q)
            for _ in range(n):
                employee, time = q.popleft()
                
                res = max(res, time)
                
                if employee in graph:
                    time_to_inform = informTime[employee]
                    q.extendleft([(report, time + time_to_inform) for report in graph[employee]])
        
        return res
