class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        totalSum = 0
        d = dict()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                curr = grid[i][j]
                totalSum += curr
                if curr not in d:
                    d[curr] = 1
                else:
                    d[curr] += 1

        # print("totalSum:", totalSum)

        shrink = totalSum
        grow = 0


        dGrow = d.copy()
        dShrink = d.copy()
        for key in dGrow:
            dGrow[key] = 0

        for i in range(len(grid)-1):
            for j in range(len(grid[i])):
                curr = grid[i][j]

                grow += curr
                shrink -= curr

                dGrow[curr] += 1
                dShrink[curr] -= 1
            if shrink == grow:
                return True
            if shrink - grow in dShrink and dShrink[shrink - grow] > 0:
                if i < len(grid)-2 and len(grid[i]) > 1:
                    return True
                # check for single
                # check the edges
                if grid[-1][0] == shrink - grow:
                    return True
                if grid[-1][-1] == shrink - grow:
                    return True
                if len(grid[0]) == 1 and grid[i+1][0] == shrink - grow:
                    return True
                # return False
                    
            if grow - shrink in dGrow and dGrow[grow - shrink] > 0:
                if i > 0 and len(grid[0]) > 1:
                    return True
                if grid[0][0] == grow - shrink:
                    return True
                if grid[0][-1] == grow - shrink:
                    return True
                if len(grid) == 1 and grid[i][0] == grow - shrink:
                    return True
                # return False
        
        shrink = totalSum
        grow = 0

        dGrow = d.copy()
        dShrink = d.copy()
        for key in dGrow:
            dGrow[key] = 0

        for j in range(len(grid[0])-1):
            lastI = 0
            for i in range(len(grid)):
                curr = grid[i][j]

                grow += curr
                shrink -= curr

                dGrow[curr] += 1
                dShrink[curr] -= 1

                lastI = i
            print(shrink, grow,j)
            if shrink == grow:
                return True
            if shrink - grow in dShrink and dShrink[shrink - grow] > 0:
                if j < len(grid[0])-2 and len(grid) > 1:
                    return True
                if grid[0][-1] == shrink - grow:
                    return True
                if grid[-1][-1] == shrink - grow:
                    return True
                if len(grid) == 1 and grid[0][j+1] == shrink - grow:
                    return True
                return False
            if grow - shrink in dGrow and dGrow[grow - shrink] > 0:
                if j > 0 and len(grid) > 1:
                    return True
                if grid[0][0] == grow - shrink:
                    return True
                if grid[-1][0] == grow - shrink:
                    return True
                if len(grid) == 1 and grid[0][j] == grow - shrink:
                    return True
                return False

        return False

        