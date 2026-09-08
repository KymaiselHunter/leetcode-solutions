class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        c = dict()
        
        for i in range(len(wall)):
            pre = 0
            for j in range(len(wall[i])-1):
                pre += wall[i][j]
                if pre not in c:
                    c[pre] = 1
                else:
                    c[pre] += 1

        out = list(c.values())
        if not out:
            return len(wall)

        # print(max(out))
        return len(wall) - max(out)