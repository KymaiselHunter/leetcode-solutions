class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                x = False
                curr = 0
                if grid[i][j] == 'X':
                    curr = 1
                    x = True
                elif grid[i][j] == 'Y':
                    curr = -1
                
                if j > 0:
                    curr += grid[i][j-1][0]

                    if grid[i][j-1][1]:
                        x = True

                grid[i][j] = (curr, x)
        # print(grid)
        out = 0

        for j in range(len(grid[0])):
            pre = 0
            x = False
            for i in range(len(grid)):
                if not x and grid[i][j][1]:
                    x = True
                pre += grid[i][j][0]
                if pre == 0 and x:
                    out += 1

        return out

                