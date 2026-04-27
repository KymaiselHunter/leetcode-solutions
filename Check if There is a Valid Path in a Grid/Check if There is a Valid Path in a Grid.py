class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        DIRS = ((1,0), (-1, 0), (0,1), (0,-1))
        streets = {
            1 : ((0,1), (0,-1)),
            2 : ((1,0), (-1,0)),
            3 : ((0,-1), (1,0)),
            4 : ((0,1), (1,0)),
            5 : ((0,-1), (-1,0)),
            6 : ((0,1), (-1,0)),
        }

        def inBounds(row:int,col:int, grid: List[List[int]]) -> bool:
            if row < 0 or col < 0:
                return False
            if row >= len(grid) or col >= len(grid[row]): 
                return False
            return True

        passed = set() 
        bfs = [(len(grid)-1, len(grid[0])-1)]

        while bfs:
            currRow, currCol = bfs.pop(0)
            if (currRow, currCol) in passed:
                continue

            if (currRow, currCol) == (0,0):
                return True

            passed.add((currRow, currCol))

            streetType = grid[currRow][currCol]
            ahead = streets[streetType]

            for dr,dc in ahead:
                nextRow, nextCol = currRow + dr, currCol + dc
                if not inBounds(nextRow, nextCol, grid):
                    continue
                if (nextRow, nextCol) in passed:
                    continue
                nextStreetType = grid[nextRow][nextCol]
                nextStreetType = streets[nextStreetType]
                if not (-dr, -dc) in nextStreetType:
                    continue
                bfs.append((nextRow, nextCol))

        return False
                