# https://leetcode.com/problems/keys-and-rooms/
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        all_rooms = set(range(len(rooms)))
        
        q = deque([0])
        while q:
            next_rooms = set()
            
            n = len(q)
            for _ in range(n):
                room = q.popleft()
                all_rooms.remove(room)
                next_rooms.update(rooms[room])
            
            for next_room in next_rooms:
                if next_room in all_rooms:
                    q.append(next_room)
        
        return len(all_rooms) == 0
