class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        target = 0
        spread = list()
        
        rowCount, colCount = len(grid), len(grid[0])

        for i in range(rowCount):
            for j in range(colCount):
                orange = grid[i][j]
                if orange == 1 or orange == 2:
                    target += 1
                if orange == 2:
                    spread.append((i,j))

        time = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        found = 0

        # print(target)

        while spread:
            # print(spread)
            currSpread = len(spread)
            found += currSpread
            if found == target:
                return time

            for i in range(currSpread):
                currentOrangeRow = spread[0][0]
                currentOrangeCol = spread[0][1]
                for d in directions:
                    rowChange = d[0]
                    colChange = d[1]

                    rotRow = currentOrangeRow + rowChange
                    rotCol = currentOrangeCol + colChange

                    if rotRow < 0 or rotRow > rowCount-1:
                        continue
                    if rotCol < 0 or rotCol > colCount-1:
                        continue
                    
                    if grid[rotRow][rotCol] == 1:
                        grid[rotRow][rotCol] = 2
                        spread.append((rotRow, rotCol))

                spread.pop(0)
            time += 1

        return -1
                    