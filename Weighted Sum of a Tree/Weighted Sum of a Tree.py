class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        d = dict()

        for i in range(len(parent)):
            root = parent[i]

            if root not in d:
                d[root] = list()

            d[root].append(i)

        print(d)
        # node, height
        bfs = [(0, 1)]
        height = 1
        while bfs:
            curr = bfs.pop(0)
            height = max(curr[1], height)

            if not curr[0] in d:
                continue
            for i in range(len(d[curr[0]])):
                bfs.append((d[curr[0]][i], curr[1]+1))

        bfs = [(0, 1)]
        out = 0
        
        while bfs:
            curr = bfs.pop(0)
            weight = height - curr[1] + 1
            weight *= nums[curr[0]]
            
            out += weight
            if not curr[0] in d:
                continue
            for i in range(len(d[curr[0]])):
                bfs.append((d[curr[0]][i], curr[1]+1))
        return out
