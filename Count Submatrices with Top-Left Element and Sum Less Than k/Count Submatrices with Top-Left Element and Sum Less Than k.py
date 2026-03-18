class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        out = 0


        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if i < len(grid)-1:
                    grid[i+1][j] += grid[i][j]
                
                # if j < len(grid[i])-1:
                #     grid[i][j+1] += grid[i][j]


        for i in range(len(grid)):
            pre = 0
            for j in range(len(grid[i])):
                if grid[i][j] + pre <= k:
                    out += 1
                    print(i,j)
                pre += grid[i][j]

        # print(grid)

        return out
