# https://leetcode.com/problems/kill-process/

from collections import defaultdict, deque

class Solution:
    def killProcess(self, pids: List[int], ppids: List[int], kill: int) -> List[int]:
        ppid_idx = defaultdict(list)
        for i, ppid in enumerate(ppids):
            ppid_idx[ppid].append(i)

        res = [kill]

        q = deque([kill])
        while q:
            n = len(q)
            for _ in range(n):
                p = q.popleft()

                for i in ppid_idx[p]:
                    res.append(pids[i])
                    q.append(pids[i])

        return res
