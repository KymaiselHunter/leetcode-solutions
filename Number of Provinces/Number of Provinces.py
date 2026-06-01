class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        v = set()
        c = 0

        for i in range(len(isConnected)):
            if i in v:
                continue

            bfs = [i]

            while bfs:
                curr = bfs.pop()
                if curr in v:
                    continue
                v.add(curr)
                for j in range(len(isConnected)):
                    if curr == j or j in v:
                        continue
                    if isConnected[curr][j] == 0:
                        continue
                    bfs.append(j)
            c += 1
        return c