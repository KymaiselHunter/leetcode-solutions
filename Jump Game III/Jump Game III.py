class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()

        bfs = list()
        bfs.append(start)

        while bfs:
            curr = bfs.pop(0)
            if curr >= len(arr) or curr < 0:
                continue
            if curr in visited:
                continue

            visited.add(curr)
            value = arr[curr]

            if value == 0:
                return True

            bfs.append(curr + value)
            bfs.append(curr - value)

        return False

            