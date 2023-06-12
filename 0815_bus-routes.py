class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stop_to_buses = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus)

        seen_buses = set()
        q = deque(stop_to_buses[source])
        res = 1
        while q:
            n = len(q)
            for _ in range(n):
                bus = q.popleft()
                if bus in seen_buses:
                    continue
                
                seen_buses.add(bus)
                                
                for stop in routes[bus]:
                    if target == stop:
                        return res
                    
                    for next_bus in stop_to_buses[stop]:
                        if next_bus in seen_buses:
                            continue
                        q.append(next_bus)
            res += 1

        return -1
