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
                if i < len(grid)-2
                    return True
                # check for single
                if grid[i+1][]
            if grow - shrink in dGrow and dGrow[grow - shrink] > 0:
                return True
        
        shrink = totalSum
        grow = 0

        dGrow = d.copy()
        dShrink = d.copy()
        for key in dGrow:
            dGrow[key] = 0

        for j in range(len(grid[0])-1):
            for i in range(len(grid)):
                curr = grid[i][j]

                grow += curr
                shrink -= curr

                dGrow[curr] += 1
                dShrink[curr] -= 1

            if shrink == grow:
                return True
            if shrink - grow in dShrink and dShrink[shrink - grow] > 0:
                return True
            if grow - shrink in dGrow and dGrow[grow - shrink] > 0:
                return True

        return False

        