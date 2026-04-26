class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        path = set()

        DIRS = ((1,0), (-1,0), (0,1), (0,-1))

        def inBounds(row: int, col: int) -> bool:
            if row < 0 or col < 0:
                return False
            nonlocal grid
            if row >= len(grid) or col >= len(grid[0]):
                return False

            return True

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                start = (row,col)
                def recur(row: int, col: int) -> bool:
                    if not inBounds(row, col):
                        return False

                    nonlocal start
                    nonlocal grid
                    if grid[row][col] != grid[start[0]][start[1]]:
                        return False

                    nonlocal path
                    if (row, col) == start:
                        if len(path) > 2:
                            return True
                    
                    if (row, col) in path:
                        return False
                    
                    path.add((row,col))
                    for dr, dc in DIRS:
                        if recur(row + dr, col + dc):
                            return True
                    path.remove((row,col))
                    

                if recur(row, col):
                    return True
        return False
