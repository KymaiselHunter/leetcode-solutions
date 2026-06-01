class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        v = set()

        bfs = [0]

        while bfs:
            curr = bfs.pop()
            if curr in v:
                continue
            v.add(curr)
            for key in rooms[curr]:
                if key in v:
                    continue
                bfs.append(key)
            
        return len(v) == len(rooms)